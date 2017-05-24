# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0008_auto_20160217_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='destination',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ports',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='speedtestresult',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
