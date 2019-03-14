# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='purchased',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
