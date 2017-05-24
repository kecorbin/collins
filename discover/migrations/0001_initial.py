# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 01:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('destination', models.CharField(max_length=25)),
                ('ports', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('results', models.CharField(blank=True, max_length=5000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
