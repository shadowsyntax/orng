# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cusrefgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refgen',
            name='letter_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
