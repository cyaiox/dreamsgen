# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream', '0004_auto_20170217_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='android_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='dream',
            name='ios_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='pack',
            name='android_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='pack',
            name='ios_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
