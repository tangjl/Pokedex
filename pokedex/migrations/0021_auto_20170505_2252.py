# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0020_auto_20170505_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='sprite',
            field=models.ImageField(null=True, upload_to='sprites'),
        ),
    ]