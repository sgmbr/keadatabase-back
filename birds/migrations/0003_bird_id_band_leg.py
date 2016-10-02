# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0002_bird_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='id_band_leg',
            field=models.CharField(blank=True, choices=[('', 'Unknown'), ('L', 'Left'), ('R', 'Right')], default='', max_length=1, verbose_name='ID band leg (primary)'),
        ),
    ]