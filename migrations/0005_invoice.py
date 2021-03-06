# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_MA_DB', '0004_auto_20161008_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('index_id', models.AutoField(primary_key=True, serialize=False)),
                ('inv_date', models.DateField(blank=True, null=True)),
                ('inv_no', models.CharField(blank=True, max_length=12, null=True)),
                ('quote_no', models.CharField(blank=True, max_length=40, null=True)),
                ('MA_staff', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('service', models.CharField(blank=True, max_length=45, null=True)),
                ('instrument', models.CharField(blank=True, max_length=45, null=True)),
                ('person', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=800, null=True)),
                ('num_sample', models.IntegerField(blank=True, null=True)),
                ('int_ext', models.CharField(blank=True, max_length=3, null=True)),
                ('state', models.CharField(blank=True, max_length=3, null=True)),
                ('country', models.CharField(blank=True, max_length=11, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
