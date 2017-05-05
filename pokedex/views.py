from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Pokemon, Stats, Region, Type, Trainer, Pokemon_List
from pprint import pprint
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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

@login_required
def pokemon_collection(request, username):
    user = get_object_or_404(User, username=request.user.username)
    trainer = get_object_or_404(Trainer, user=request.user)
    pprint(trainer)
    pokemon_list = Pokemon_List.objects.filter(user=trainer).values_list('pokemon', flat=True)
    pokemon_group = []
    for pokemon in pokemon_list:
        pokemon_group.append(pokemon-5)
        pprint(pokemon)
    pokemons = Pokemon.objects.filter(number__in=pokemon_group)
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})