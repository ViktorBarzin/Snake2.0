from __future__ import unicode_literals
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from authentication.models import Profile


class Lobby(models.Model):
    id = models.AutoField(primary_key=True)
    is_full = models.BooleanField()

class Profile(User):
    lobby = models.ForeignKey(Lobby, related_name='users', on_delete=models.PROTECT, null=True, blank=True)
    lobby_owned = models.OneToOneField(Lobby, related_name='owner', on_delete=models.PROTECT, null=True, blank=True)
