from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    objects: UserManager()
    boj_id = models.CharField(max_length=100, blank=False)
