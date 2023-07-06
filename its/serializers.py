from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from its.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']

    @atomic
    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        Contributor.objects.create(user_id=self.context["request"].user,
                                   project_id=project,
                                   permission=Contributor.READ_WRITE,
                                   role=Contributor.AUTHOR)
        return project


class ContributorSerializer(ModelSerializer):
    user_id = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['id', 'user_id']
        read_only_fields = ['id', 'user_id']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['project_id', 'author_user_id', 'assignee_user_id', 'created_time']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time']
