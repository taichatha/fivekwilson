# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0012_auto_20151129_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('car', models.OneToOneField(to='customerdb.Car')),
                ('customer', models.OneToOneField(to='customerdb.Customer')),
                ('employee', models.OneToOneField(to='customerdb.Employee')),
                ('work', models.ForeignKey(to='customerdb.Work')),
            ],
        ),
    ]
