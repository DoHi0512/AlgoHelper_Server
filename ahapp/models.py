
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    bojid = models.CharField(max_length=20)


class Problem(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
