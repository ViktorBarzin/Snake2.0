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
    # TODO: null=True on owner is not a good idea;
    # consider making some sort of superuser the default owner of all lobbies?
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


# Profile should be in another module but due to circular import errors it is here..
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE, null=True, related_name='users')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
