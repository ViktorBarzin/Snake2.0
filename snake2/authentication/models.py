from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from lobby.models import Lobby
# Create your models here.


class Profile(User):
    lobby = models.ForeignKey(Lobby, related_name='users', on_delete=models.PROTECT, null=True, blank=True)
    lobby_owned = models.OneToOneField(Lobby, related_name='owner', on_delete=models.PROTECT, null=True, blank=True)

    games_won = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    win_ratio = models.FloatField(default=0)
    # date_joined = models.DateTimeField()
    profile_picture_url = models.CharField(max_length=255,null=True)

    def get_win_ratio(self):
        if games_played == 0:
            return 0
        return games_won / games_played
