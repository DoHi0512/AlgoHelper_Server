from tabnanny import verbose
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, boj_id, password):
        user = self.model(
            username=username,
            boj_id=boj_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, boj_id, password):
        user = self.create_user(
            username=username,
            password=password,
            boj_id=boj_id
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    boj_id = models.CharField(max_length=100)
    objects = UserManager()

    class Meta:
        db_table = 'user'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
