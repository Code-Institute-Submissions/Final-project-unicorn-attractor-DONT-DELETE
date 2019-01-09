# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0009_auto_20190104_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugstatus',
            name='status',
            field=models.CharField(choices=[('Doing', 'Doing'), ('Done', 'Done')], default='Todo', max_length=10),
        ),
    ]