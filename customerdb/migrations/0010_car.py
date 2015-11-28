# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0009_auto_20151128_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(max_length=100, blank=True)),
                ('model', models.CharField(max_length=100, blank=True)),
                ('year', models.CharField(max_length=100, blank=True)),
                ('plate', models.CharField(max_length=100, blank=True)),
                ('vin', models.CharField(max_length=100, blank=True)),
                ('customer', models.ForeignKey(default=False, to='customerdb.Customer')),
            ],
        ),
    ]
