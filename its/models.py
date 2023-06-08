from django.db import models

from authentication.models import Contributor, User


class Project(models.Model):
    BACKEND = "BK"
    FRONTEND = "FT"
    IOS = "IO"
    ANDROID = "AD"
    TYPES_CHOICES = [
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android")
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=2, choices=TYPES_CHOICES)
    author_user_id = models.ForeignKey(Contributor, on_delete=models.CASCADE)


class Issue(models.Model):
    LOW = "LW"
    MEDIUM = "MD"
    HIGH = "HG"
    BUG = "BUG"
    IMPROVEMENT = "IMP"
    TASK = "TSK"
    TO_DO = "TODO"
    IN_PROGRESS = "INPG"
    DONE = "DONE"

    PRIORITY_CHOICES = [
        (LOW, "FAIBLE"),
        (MEDIUM, "MOYENNE"),
        (HIGH, "ÉLEVÉE")
    ]
    TAG_CHOICES = [
        (BUG, "BUG"),
        (IMPROVEMENT, "AMÉLIORATION"),
        (TASK, "TÂCHE")
    ]
    STATUS_CHOICES = [
        (TO_DO, "À faire"),
        (IN_PROGRESS, "En cours"),
        (DONE, "Terminé")
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=3, choices=TAG_CHOICES)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    project_id = models.IntegerField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=author_user_id, related_name="assignee")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField()
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
