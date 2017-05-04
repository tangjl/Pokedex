# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-04 21:16
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='strength',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], max_length=71, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='weakness',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], max_length=71, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='pokemon_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NOR', 'Normal'), ('FIG', 'Fighting'), ('FLY', 'Flying'), ('POI', 'Poison'), ('GRO', 'Ground'), ('ROC', 'Rock'), ('BUG', 'Bug'), ('GHO', 'Ghost'), ('FIR', 'Fire'), ('WAT', 'Water'), ('GRA', 'Grass'), ('ELE', 'Electric'), ('PSY', 'Psychic'), ('ICE', 'Ice'), ('DRA', 'Dragon'), ('DAR', 'Dark'), ('STE', 'Steel'), ('FAI', 'Fairy')], max_length=71),
        ),
    ]
