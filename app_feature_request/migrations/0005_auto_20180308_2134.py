# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_feature_request', '0004_auto_20180307_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurereq',
            name='productarea',
            field=models.CharField(choices=[('Billing', 'billing'), ('Policies', 'policies'), ('Claims', 'claims'), ('Reports', 'reports')], max_length=15),
        ),
    ]