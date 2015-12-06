# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0014_auto_20151129_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='car',
            field=models.ForeignKey(to='customerdb.Car', blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='work',
            field=models.ForeignKey(to='customerdb.Work', blank=True),
        ),
    ]
