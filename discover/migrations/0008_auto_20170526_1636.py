# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0007_remove_speedtest_job'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Scan',
        ),
    ]
