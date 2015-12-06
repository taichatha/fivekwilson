# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0018_auto_20151205_1924'),
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
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_work', models.CharField(max_length=100, blank=True)),
                ('cost', models.CharField(max_length=100, blank=True)),
                ('appointment', models.ForeignKey(to='customerdb.Appointment', blank=True)),
            ],
        ),
    ]
