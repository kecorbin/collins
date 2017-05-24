# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fqdn', models.CharField(default=b'connect.greenlightcontrol.com', max_length=50)),
                ('user', models.CharField(default=b'janus', max_length=10)),
                ('key', models.TextField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=80)),
                ('version', models.CharField(default=b'unknown', max_length=16)),
                ('lanip', models.GenericIPAddressField(null=True, blank=True)),
                ('wanip', models.CharField(default=b'unknown', max_length=32)),
                ('hostname', models.CharField(unique=True, max_length=64)),
                ('pubkey', models.CharField(max_length=512, null=True, blank=True)),
                ('privkey', models.CharField(max_length=512, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('healthy', models.BooleanField(default=False)),
                ('last_tested', models.DateTimeField(auto_now=True, null=True)),
                ('polling_interval', models.SmallIntegerField(default=15)),
                ('cloudserver', models.ForeignKey(blank=True, to='connect.CloudServer', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proxyport', models.SmallIntegerField()),
                ('inuse', models.BooleanField(default=False)),
                ('cloudserver', models.ForeignKey(blank=True, to='connect.CloudServer', null=True)),
                ('gateway', models.ForeignKey(blank=True, to='connect.Gateway', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sourceip', models.GenericIPAddressField(default=b'0.0.0.0')),
                ('remoteport', models.IntegerField()),
                ('remotehost', models.CharField(max_length=128)),
                ('timeout', models.SmallIntegerField(default=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(null=True, blank=True)),
                ('processed', models.BooleanField(default=False)),
                ('url', models.URLField(default=None, null=True, blank=True)),
                ('gateway', models.ForeignKey(blank=True, to='connect.Gateway', null=True)),
                ('proxyport', models.OneToOneField(null=True, blank=True, to='connect.ProxyPort')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
