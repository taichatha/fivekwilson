# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0008_car_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
