from django.shortcuts import render
from .models import Pokemon, Stats
from .filters import PokeFilter

def pokemon_list(request):
    pokemons = Pokemon.objects.order_by('number')
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

def search(request):
    pokemon_list = Pokemon.objects.order_by('number')
    pokemons = PokeFilter(request.GET, queryset=pokemon_list)
    return render(request, 'search/pokemon_list.html', {'pokemons': pokemons})

