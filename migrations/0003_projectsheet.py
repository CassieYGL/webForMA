# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_MA_DB', '0002_auto_20160929_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSheet',
            fields=[
                ('title', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('file_path', models.FileField(upload_to='')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
