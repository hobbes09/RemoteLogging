# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20160606_1035'),
        ('log', '0006_auto_20160605_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='session.Session', verbose_name=b'session'),
        ),
    ]
