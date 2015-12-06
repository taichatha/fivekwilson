# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0016_auto_20151205_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(to='customerdb.Car', blank=True)),
                ('customer', models.ForeignKey(to='customerdb.Customer')),
                ('employee', models.ForeignKey(to='customerdb.Employee')),
                ('work', models.ForeignKey(to='customerdb.Work', blank=True)),
            ],
        ),
    ]
