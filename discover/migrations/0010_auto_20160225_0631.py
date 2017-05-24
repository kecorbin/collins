# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0009_auto_20160225_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedtestresult',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
