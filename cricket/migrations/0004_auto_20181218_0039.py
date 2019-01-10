# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_auto_20181217_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'unsure', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='pcteam',
            name='club',
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.RemoveField(
            model_name='club',
            name='pc_id',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='pc_id',
        ),
        migrations.RemoveField(
            model_name='ground',
            name='pc_id',
        ),
        migrations.RemoveField(
            model_name='match',
            name='fk_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='umpire',
            name='pc_id',
        ),
        migrations.AlterField(
            model_name='match',
            name='fk_away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='cricket.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='fk_home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='cricket.Team'),
        ),
        migrations.DeleteModel(
            name='PCTeam',
        ),
        migrations.DeleteModel(
            name='PlayCricketTeam',
        ),
        migrations.AddField(
            model_name='team',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.Club'),
        ),
    ]
