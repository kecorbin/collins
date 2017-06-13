# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 02:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_auto_20170601_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='authorized_users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
