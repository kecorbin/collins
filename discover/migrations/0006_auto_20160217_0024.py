# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0005_auto_20160216_2228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BandwidthTestResult',
            new_name='SpeedTestResult',
        ),
    ]
