# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0004_customer_email'),
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
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
