# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publishedAt',
            field=models.CharField(blank=True, default='Not available', max_length=100, null=True),
        ),
    ]