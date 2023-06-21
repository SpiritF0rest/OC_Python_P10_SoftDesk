from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import filters, status

from authentication.models import User
from its.models import Project, Contributor, Issue, Comment
from its.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title']
    search_fields = ['type']
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        projects_list = Contributor.objects.filter(user_id=self.request.user).values_list('project_id')
        queryset = Project.objects.filter(id__in=projects_list)
        return queryset


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Contributor.objects.filter(project_id=self.kwargs['project_id'])  # .values_list('user_id')
        # queryset = User.objects.filter(id__in=users_list)
        return queryset

    def create(self, request, *args, **kwargs):
        request.data["project_id"] = self.kwargs['project_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Issue.objects.filter(project_id=self.kwargs['project_id'])
        return queryset


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.filter(issue_id=self.kwargs['issue_id'])
        return queryset
