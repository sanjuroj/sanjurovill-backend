# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20160506_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='doi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='award',
            name='summary',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='publication',
            name='summary',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='summary',
            field=models.TextField(max_length=255),
        ),
    ]
