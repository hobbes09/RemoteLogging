# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('type', models.CharField(choices=[(b'A', b'ASSERT'), (b'D', b'DEBUG'), (b'E', b'ERROR'), (b'I', b'INFO'), (b'V', b'VERBOSE'), (b'W', b'WARN')], default=b'V', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
