# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cusrefgen', '0003_auto_20161023_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='refgen',
            name='org_units',
            field=models.CharField(choices=[('AA', 'Admin Services'), ('CF', 'Chief Finance Office'), ('CS', 'Corporate Services'), ('KE', 'Customer Care'), ('SO', 'Data Centre Operations'), ('FI', 'Finance'), ('EA', 'Group Managing Director'), ('HC', 'Human Capital Management'), ('SA', 'Information Systems & Technology'), ('ME', 'Media & Entertainment'), ('MA', 'Marketing'), ('GJ', 'Network Infrastructure Unit'), ('NS', 'Network Services Division'), ('PD', 'Product Development'), ('PM', 'Program Management'), ('RD', 'Research & Development'), ('SC', 'Supply Chain Management')], default='Select from below', max_length=50),
        ),
    ]
