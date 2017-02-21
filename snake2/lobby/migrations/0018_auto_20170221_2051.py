# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0017_remove_profile_asd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lobby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='lobby.Lobby'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lobby_owned',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='lobby.Lobby'),
        ),
    ]