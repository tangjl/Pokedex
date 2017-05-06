# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0017_pokemon_statistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='statistics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='pokedex.Stats'),
        ),
    ]
