# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_scheduler_restart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='last_result',
        ),
    ]
