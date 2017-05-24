# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_remove_proxyport_gateway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudserver',
            name='fqdn',
            field=models.CharField(default=b'connect.greenlightcontrol.com', unique=True, max_length=50),
        ),
    ]
