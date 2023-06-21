from rest_framework.serializers import ModelSerializer

from its.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        Contributor.objects.create(user_id=self.context["request"].user,
                                   project_id=project,
                                   permission=Contributor.READ_WRITE,
                                   role=Contributor.AUTHOR)
        return project


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'project_id']

    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name']

    def create(self, validated_data):
        # project = Project.objects.get(id=self.context['view'].kwargs['project_id'])
        contributor = Contributor.objects.create(**validated_data,
                                                 user_id=self.context["request"].user,
                                                 permission=Contributor.READ_ONLY,
                                                 role=Contributor.CONTRIBUTOR)
        return contributor


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status']

    def create(self, validated_data):
        project = Project.objects.get(id=self.context['view'].kwargs['project_id'])
        assignee = self.context["request"].user if "assignee_user_id" not in validated_data \
            else validated_data["assignee_user_id"]
        issue = Issue.objects.create(**validated_data,
                                     project_id=project,
                                     assignee_user_id=assignee,
                                     author_user_id=self.context["request"].user)
        return issue


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time']

    def create(self, validated_data):
        issue = Issue.objects.get(id=self.context['view'].kwargs['issue_id'])
        comment = Comment.objects.create(**validated_data,
                                         issue_id=issue,
                                         author_user_id=self.context["request"].user)
        return comment
