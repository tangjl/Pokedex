from django.shortcuts import render
from .models import Pokemon, Stats
from django.http import HttpResponse 

def pokemon_list(request):
    pokemons = Pokemon.objects.order_by('number')
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

