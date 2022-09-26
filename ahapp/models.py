from asyncio.windows_events import NULL

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, password, **extra_fields):
        user = self.model(
            name=name, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, unique=True)
    boj_id = models.CharField(max_length=100)
    problem = models.CharField(max_length=32000 , default=NULL)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['boj_id', ]

    objects = UserManager()

    def __str__(self):
        return self.name



