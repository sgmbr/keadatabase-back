# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0015_remove_sightingssighting_revisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightingsmedia',
            name='birds',
            field=models.ManyToManyField(blank=True, to='birds.Bird', verbose_name='Birds in image'),
        ),
    ]
