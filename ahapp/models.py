import imp
from operator import mod
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


# class Book(models.Model):
#     bid = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)
#     category = models.CharField(max_length=50)
#     pages = models.IntegerField()
#     price = models.IntegerField()
#     published_date = models.DateField()
#     description = models.TextField()


# class Users(models.Model):
#     userName = models.CharField(max_length=20)
#     pwd = models.CharField(max_length=20)
#     bojId = models.CharField(max_length=20, null=True)

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    bojid = models.CharField(max_length=20)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
