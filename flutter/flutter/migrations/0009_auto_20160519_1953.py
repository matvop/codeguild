# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0008_auto_20160519_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='comment',
            field=models.CharField(max_length=400),
        ),
    ]