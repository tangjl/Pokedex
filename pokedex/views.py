from django.shortcuts import render, render_to_response
from .models import Pokemon, Stats, Region, Type
from .forms import PokemonForm
from pprint import pprint
from django.http import HttpResponse 
from django.db.models import Q


def pokemon_list(request):
    pokemons = Pokemon.objects.order_by('number')
    #pprint(Pokemon.objects.all())
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

def search(request):
    namer = request.GET.get('q')
    regionr = request.GET.get('regiontype')
    climater = request.GET.get('climatetype')
    typer = request.GET.get('typetype')

    regionid = Region.objects.filter(region_name=regionr)
    typeid = Type.objects.filter(pokemon_type__contains=typer)
    pokemons = Pokemon.objects.filter(name=namer,region_id=regionid,climate=climater,type_id=typeid)
    if len(Pokemon.objects.filter(name=namer,region_id=regionid,climate=climater,type_id=typeid)) == 0:
        pokemons = Pokemon.objects.order_by('number')
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})
