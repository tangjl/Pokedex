from django.shortcuts import render, render_to_response
from .models import Pokemon, Stats
from pprint import pprint
from django.http import HttpResponse 


def pokemon_list(request):
    pokemons = Pokemon.objects.order_by('number')
    #pprint(Pokemon.objects.all())
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

def search(request):
    query = request.GET.get('q')
    pokemons = Pokemon.objects.filter(name=query)
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})
