# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 22:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('addiction', '0002_auto_20170316_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addictions',
            name='recorded_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 15, 22, 10, 16, 898907, tzinfo=utc), editable=False),
        ),
    ]
