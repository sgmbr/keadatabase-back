# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 03:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_auto_20161117_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='band_colour',
        ),
        migrations.RemoveField(
            model_name='band',
            name='band_symbol',
        ),
        migrations.RemoveField(
            model_name='band',
            name='primary_location',
        ),
    ]