# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0008_bugstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugstatus',
            name='status',
            field=models.CharField(choices=[('To do', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], default='Todo', max_length=10),
        ),
    ]
