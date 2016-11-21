# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_homelocation'),
        ('birds', '0009_bird_band_combo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bird',
            name='primary_location',
        ),
        migrations.RemoveField(
            model_name='bird',
            name='secondary_location',
        ),
        migrations.AddField(
            model_name='bird',
            name='home_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.HomeLocation'),
        ),
    ]
