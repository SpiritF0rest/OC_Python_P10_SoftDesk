from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


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
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    permission = models.CharField(max_length=2, choices=PERMISSION_CHOICES, default=None)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
