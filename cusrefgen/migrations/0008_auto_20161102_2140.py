# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cusrefgen', '0007_auto_20161102_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refgen',
            name='ref_number',
            field=models.IntegerField(),
        ),
    ]
