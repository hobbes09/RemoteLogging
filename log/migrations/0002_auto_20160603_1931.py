# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
