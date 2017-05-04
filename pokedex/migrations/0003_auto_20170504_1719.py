# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_auto_20170504_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='climate',
            field=models.CharField(choices=[('GR', 'Grassy'), ('MO', 'Mountain'), ('BU', 'Building'), ('SN', 'Snow'), ('WA', 'Water'), ('DE', 'Desert')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Climate',
        ),
    ]
