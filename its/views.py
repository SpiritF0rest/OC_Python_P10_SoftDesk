from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from its.models import Project, Contributor, Issue, Comment
from its.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        projects_list = Contributor.objects.filter(user_id=self.request.user).values_list('project_id')
        queryset = Project.objects.filter(id__in=projects_list)
        return queryset


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Contributor.objects.select_related("user_id").filter(project_id=self.kwargs['project_id'])
        return queryset

    def perform_create(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        if Contributor.objects.filter(project_id=project, user_id=self.request.user).exists():
            raise ValidationError('You are already a contributor of this project')
        serializer.save(project_id=project, user_id=self.request.user)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Issue.objects.filter(project_id=self.kwargs['project_id'])
        return queryset

    def perform_create(self, serializer):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        assignee = self.request.user
        if "assignee_user_id" in self.request.data and self.request.data["assignee_user_id"] != "":
            assignee = get_object_or_404(User, id=self.request.data["assignee_user_id"])
        serializer.save(project_id=project, author_user_id=self.request.user, assignee_user_id=assignee)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.filter(issue_id=self.kwargs['issue_id'])
        return queryset

    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, id=self.kwargs['issue_id'])
        serializer.save(author_user_id=self.request.user, issue_id=issue)
