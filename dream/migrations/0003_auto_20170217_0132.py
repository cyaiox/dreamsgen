# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dream', '0002_auto_20170207_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('is_available', models.BooleanField()),
                ('price', models.FloatField()),
                ('android_code', models.CharField(max_length=64)),
                ('ios_code', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameField(
            model_name='dream',
            old_name='status',
            new_name='is_available',
        ),
        migrations.RenameField(
            model_name='frame',
            old_name='status',
            new_name='is_available',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='status',
            new_name='is_available',
        ),
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dream.Group'),
        ),
        migrations.AddField(
            model_name='pack',
            name='dreams',
            field=models.ManyToManyField(to='dream.Dream'),
        ),
        migrations.AddField(
            model_name='library',
            name='dream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dream.Dream'),
        ),
        migrations.AddField(
            model_name='library',
            name='pack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dream.Pack'),
        ),
        migrations.AddField(
            model_name='library',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
