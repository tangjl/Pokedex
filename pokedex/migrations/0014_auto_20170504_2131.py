# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0013_auto_20170504_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='climate',
            field=models.CharField(choices=[('GR', 'Grassy'), ('MO', 'Mountain'), ('BU', 'Building'), ('SN', 'Snow'), ('OC', 'Ocean'), ('DE', 'Desert'), ('SK', 'Sky')], max_length=2),
        ),
    ]