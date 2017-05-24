# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20170511_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='json',
            field=jsonfield.fields.JSONField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]