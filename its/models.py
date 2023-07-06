from django.db import models

from authentication.models import User


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
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    assignee_user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assignee")
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField()
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    READ_ONLY = "RO"
    READ_WRITE = "RW"
    AUTHOR = "AU"
    CONTRIBUTOR = "CO"

    PERMISSION_CHOICES = [
        (READ_ONLY, "droit de lecture seulement"),
        (READ_WRITE, "droit de lecture et écriture")
    ]
    ROLE_CHOICES = [
        (AUTHOR, "auteur"),
        (CONTRIBUTOR, "contributeur")
    ]
    user_id = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=2, choices=PERMISSION_CHOICES, default=READ_ONLY)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=CONTRIBUTOR)
