# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteEngine', '0005_auto_20160622_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertype',
            name='order_type',
        ),
        migrations.RemoveField(
            model_name='tickettype',
            name='ticket_type',
        ),
    ]
