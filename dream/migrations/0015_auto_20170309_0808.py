# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream', '0014_auto_20170309_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='image_source',
            field=models.FileField(blank=True, upload_to=b'frames/', verbose_name=b'Image Source'),
        ),
    ]
