# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taekwondo', '0005_auto_20161016_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='tf_id',
            new_name='itf_id',
        ),
    ]
