# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lynjay', '0002_auto_20171017_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
