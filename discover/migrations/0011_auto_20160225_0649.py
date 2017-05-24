# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0010_auto_20160225_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedtestresult',
            name='destination',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='speedtestresult',
            name='ports',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='speedtestresult',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
