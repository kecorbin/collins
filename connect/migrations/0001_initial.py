# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 19:45
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
            name='CloudServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fqdn', models.CharField(default=b'connect.greenlightcontrol.com', max_length=50, unique=True)),
                ('user', models.CharField(default=b'janus', max_length=10)),
                ('key', models.TextField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=80)),
                ('version', models.CharField(default=b'unknown', max_length=16)),
                ('lanip', models.GenericIPAddressField(blank=True, null=True)),
                ('wanip', models.CharField(default=b'unknown', max_length=32)),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('pubkey', models.CharField(blank=True, max_length=512, null=True)),
                ('privkey', models.CharField(blank=True, max_length=512, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('healthy', models.BooleanField(default=False)),
                ('upgrade', models.BooleanField(default=False)),
                ('last_tested', models.DateTimeField(auto_now=True, null=True)),
                ('polling_interval', models.SmallIntegerField(default=15)),
                ('cloudserver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='connect.CloudServer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxyport', models.IntegerField()),
                ('inuse', models.BooleanField(default=False)),
                ('cloudserver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='connect.CloudServer')),
            ],
        ),
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceip', models.GenericIPAddressField(default=b'0.0.0.0')),
                ('remoteport', models.IntegerField()),
                ('remotehost', models.CharField(max_length=128)),
                ('timeout', models.SmallIntegerField(default=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('processed', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('gateway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='connect.Gateway')),
                ('proxyport', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='connect.ProxyPort')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='proxyport',
            unique_together=set([('cloudserver', 'proxyport')]),
        ),
    ]
