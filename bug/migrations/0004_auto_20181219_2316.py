# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_auto_20181218_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]