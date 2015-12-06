# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0017_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='car',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='work',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
