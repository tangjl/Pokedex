# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_remove_trainer_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='sprite',
            field=models.ImageField(null=True, upload_to='sprites'),
        ),
    ]
