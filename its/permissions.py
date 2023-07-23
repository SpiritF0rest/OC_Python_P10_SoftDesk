from rest_framework import permissions

from its.models import Contributor


class AuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "destroy"]:
            if view.basename in ["issues", "comments"]:
                if obj.author_user_id == request.user:
                    return True
            if view.basename == "contributors":
                if obj.user_id == request.user:
                    return True
            if view.basename == "projects":
                is_author = Contributor.objects.filter(project_id=obj.id,
                                                       user_id=request.user,
                                                       role="AU").exists()
                return is_author
            return False
        if view.basename in ["projects", "comments"] and view.action == "retrieve":
            return True
        return False


class ContributorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.basename in ["projects", "contributors"] and view.action == "create":
            return True
        elif view.basename == "projects" and view.action == "list":
            return True
        elif view.action in ["update", "destroy"]:
            return True
        elif view.basename == "projects" and view.action == "retrieve":
            is_contributor = Contributor.objects.filter(project_id=request.parser_context["kwargs"]["pk"],
                                                        user_id=request.user).exists()
            return is_contributor
        else:
            is_contributor = Contributor.objects.filter(project_id=request.parser_context["kwargs"]["project_id"],
                                                        user_id=request.user).exists()
            return is_contributor
