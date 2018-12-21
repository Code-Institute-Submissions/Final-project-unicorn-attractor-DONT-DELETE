# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 23:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bug', '0004_auto_20181219_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bug',
            name='comment',
        ),
        migrations.AddField(
            model_name='bug',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bugcomment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bug.Bug'),
        ),
    ]
