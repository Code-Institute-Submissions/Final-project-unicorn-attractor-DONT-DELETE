# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-07 22:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('feature', '0005_auto_20190107_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featurecomment',
            old_name='Feature',
            new_name='feature',
        ),
    ]
