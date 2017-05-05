from django.shortcuts import render
from .models import Pokemon, Stats

def pokemon_list(request):
    pokemons = Pokemon.objects.order_by('number')
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})