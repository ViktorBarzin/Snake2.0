# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170220_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lobby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='lobby.Lobby'),
        ),
    ]