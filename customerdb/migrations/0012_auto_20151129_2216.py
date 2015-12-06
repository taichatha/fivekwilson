# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0011_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
