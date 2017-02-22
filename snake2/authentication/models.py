from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from lobby.models import Lobby
# Create your models here.


class Profile(User):
    lobby = models.ForeignKey(Lobby, related_name='users', on_delete=models.PROTECT, null=True, blank=True)
    lobby_owned = models.OneToOneField(Lobby, related_name='owner', on_delete=models.PROTECT, null=True, blank=True)
