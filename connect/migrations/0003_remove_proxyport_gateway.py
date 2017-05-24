# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_gateway_upgrade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxyport',
            name='gateway',
        ),
    ]
