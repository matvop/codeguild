# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flutt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(blank=True, default='Anonymous')),
                ('flutt_created_date', models.DateTimeField(auto_now=True)),
                ('flutt_text', models.TextField()),
            ],
        ),
    ]
