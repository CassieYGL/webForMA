# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_MA_DB', '0007_invoicesheet'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='invoicesheet',
            table='InvoiceSheet',
        ),
    ]
