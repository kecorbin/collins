# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0007_auto_20170608_0243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gateway',
            options={'permissions': (('view_gateway', 'View gateway'),)},
        ),
    ]