from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from PIL import Image

from lobby.models import Lobby
# Create your models here.


class Profile(User):
    lobby = models.ForeignKey(Lobby, related_name='users', on_delete=models.PROTECT, null=True, blank=True)
    lobby_owned = models.OneToOneField(Lobby, related_name='owner', on_delete=models.PROTECT, null=True, blank=True)

    games_won = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    win_ratio = models.FloatField(default=0)
    # date_joined = models.DateTimeField()
    profile_picture_url = models.ImageField(upload_to='static/media/images/', default='static/media/images/images.jpg')

    def get_win_ratio(self):
        if games_played == 0:
            return 0
        return games_won / games_played

    def set_field(self, new_field_dict):
        key = list(new_field_dict.keys())[0]
        value = new_field_dict[key]
        if hasattr(self, key):
            return self.key
        setattr(self, key, value)
        return self.__dict__[key]
