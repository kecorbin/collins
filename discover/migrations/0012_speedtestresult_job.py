# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0011_auto_20160225_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedtestresult',
            name='job',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discover.Job'),
        ),
    ]