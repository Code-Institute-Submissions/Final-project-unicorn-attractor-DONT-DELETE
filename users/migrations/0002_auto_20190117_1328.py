# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-17 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]
