# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Oniric Alarm'), (2, 'Relaxing'), (3, 'Dreams')])),
                ('description', models.CharField(max_length=128)),
                ('source', models.CharField(max_length=64)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
