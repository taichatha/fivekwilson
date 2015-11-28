# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdb', '0006_car_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
    ]
