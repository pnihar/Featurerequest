# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feature_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurereq',
            name='productarea',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='featurereq',
            name='target_date',
            field=models.DateField(),
        ),
    ]
