# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 22:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feature_request', '0005_auto_20180308_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurereq',
            name='target_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 22, 26, 51, 183346)),
        ),
    ]
