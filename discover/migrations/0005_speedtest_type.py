# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0004_auto_20170526_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedtest',
            name='type',
            field=models.CharField(default='speedtest', max_length=25),
            preserve_default=False,
        ),
    ]
