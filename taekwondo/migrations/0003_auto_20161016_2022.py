# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taekwondo', '0002_auto_20161016_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sex',
            old_name='sex',
            new_name='name',
        ),
    ]
