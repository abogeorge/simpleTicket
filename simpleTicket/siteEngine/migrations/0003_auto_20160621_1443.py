# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteEngine', '0002_auto_20160621_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='supervisor_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='siteEngine.UserProfile'),
        ),
    ]
