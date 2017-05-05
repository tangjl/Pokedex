from django import forms
from django.forms import ModelForm
from .models import Pokemon

class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ('region','type','climate',)