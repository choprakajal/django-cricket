# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-10 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0006_inning_inning_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mvpperformance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='mvpperformance',
            name='player',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_id',
        ),
        migrations.DeleteModel(
            name='MVPPerformance',
        ),
    ]
