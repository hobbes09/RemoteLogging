# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.CharField(editable=False, max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
