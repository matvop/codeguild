# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0005_auto_20160519_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutt',
            name='comment',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='flutt',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
