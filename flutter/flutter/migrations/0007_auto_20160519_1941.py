# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 02:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flutter', '0006_auto_20160519_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flutt',
            old_name='created_date',
            new_name='datetime',
        ),
    ]
