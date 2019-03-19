# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 21:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20190314_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_username',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='purchased',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
    ]
