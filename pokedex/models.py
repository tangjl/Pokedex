from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField(validators=[MaxValueValidator(802)])
    sprite = models.ImageField(upload_to='sprites', null=True)
    evolves_into = models.ForeignKey('self', related_name='ev_into', blank=True, null=True)
    evolves_from = models.ForeignKey('self', related_name='ev_from', blank=True, null=True)
    region = models.ForeignKey('Region')
    type = models.ForeignKey('Type')
    climate_choices = (
        ('GR', 'Grassy'),
        ('MO', 'Mountain'),
        ('BU', 'Building'),
        ('SN', 'Snow'),
        ('WA', 'Water'),
        ('DE', 'Desert')    
    )
    climate = models.CharField(
        max_length=2,
        choices=climate_choices
    )

    def __str__(self):
        return self.name

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    region = models.ForeignKey('Region')

    def __str__(self):
        return self.name

class Pokemon_List(models.Model):
    user = models.ForeignKey('Trainer')
    pokemon = models.ForeignKey('Pokemon', null=True)

    def __str__(self):
        return self.user.name

class Region(models.Model):
    region_name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.region_name

class Stats(models.Model):
    pokemon_id = models.ForeignKey('Pokemon', null=True)
    hp = models.IntegerField(validators=[MaxValueValidator(255)])
    attack = models.IntegerField(validators=[MaxValueValidator(255)])
    defense = models.IntegerField(validators=[MaxValueValidator(255)])
    special_attack = models.IntegerField(validators=[MaxValueValidator(255)])
    special_defense = models.IntegerField(validators=[MaxValueValidator(255)])
    speed = models.IntegerField(validators=[MaxValueValidator(255)])

    def __str__(self):
        return str(self.pokemon_id.number)   

class Type(models.Model):
    type_choices = (
        ('NOR', 'Normal'),
        ('FIG', 'Fighting'),
        ('FLY', 'Flying'),
        ('POI', 'Poison'),
        ('GRO', 'Ground'),
        ('ROC', 'Rock'),
        ('BUG', 'Bug'),
        ('GHO', 'Ghost'),
        ('FIR', 'Fire'),
        ('WAT', 'Water'),
        ('GRA', 'Grass'),
        ('ELE', 'Electric'),
        ('PSY', 'Psychic'),
        ('ICE', 'Ice'),
        ('DRA', 'Dragon'),
        ('DAR', 'Dark'),
        ('STE', 'Steel'),
        ('FAI', 'Fairy'),
    )
    pokemon_type = MultiSelectField(
        max_choices=2,
        choices=type_choices
    )
    weakness = MultiSelectField(
        max_choices=18,
        choices=type_choices,
        null=True
    )
    strength = MultiSelectField(
        max_choices=18,
        choices=type_choices,
        null=True
    )

    def __str__(self):
        return "/".join(self.pokemon_type)