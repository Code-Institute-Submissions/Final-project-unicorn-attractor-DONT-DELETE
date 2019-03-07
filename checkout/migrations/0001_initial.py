# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('feature', '0007_auto_20190109_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=50)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=40)),
                ('street_address2', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('feature', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='feature.Feature')),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='checkout.Order')),
            ],
        ),
    ]
