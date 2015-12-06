# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0013_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='car',
            field=models.ForeignKey(to='customerdb.Car'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(to='customerdb.Customer'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='employee',
            field=models.ForeignKey(to='customerdb.Employee'),
        ),
    ]
