# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dream', '0011_auto_20170302_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='dream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='dream.Dream', verbose_name=b'Dream'),
        ),
    ]