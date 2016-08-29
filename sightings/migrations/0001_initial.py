# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 09:20
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('newsletter', models.BooleanField()),
                ('category', models.CharField(blank=True, choices=[('', ''), ('TO', 'Tourist'), ('LO', 'Local'), ('SC', 'School group'), ('CG', 'Community group'), ('TR', 'Tramper'), ('HU', 'Hunter'), ('BI', 'Birder'), ('DO', 'DOC Staff'), ('OT', 'Other')], default='', max_length=2)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_sighted', models.DateField()),
                ('time_sighted', models.TimeField()),
                ('number_sighted', models.IntegerField(blank=True)),
                ('point_location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('point_accuracy', models.CharField(blank=True, choices=[('', 'Unknown'), ('G', 'GPS coordinates'), ('E', 'Estimate from map'), ('O', 'Other')], default='', max_length=1)),
                ('primary_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.PrimaryLocation')),
                ('secondary_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.SecondaryLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]