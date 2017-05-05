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
    choice = request.GET.get('sorttype')

    regionid = Region.objects.filter(region_name=regionr)
    typeid = Type.objects.filter(pokemon_type__contains=typer)
    pokemons = Pokemon.objects.order_by('number')
    ################# NO NAME CASES FIRST ##############
    if not namer and not climater and not typer and regionr:
        pokemons = Pokemon.objects.filter(region_id=regionid)
        print("1")
    elif not namer and not climater and typer and not regionr:
        pokemons = Pokemon.objects.filter(type_id=typeid)
        print("2")
    elif not namer and climater and not typer and not regionr:
        pokemons = Pokemon.objects.filter(climate=climater)
        print("3")
    elif not namer and not climater and typer and regionr:
        pokemons = Pokemon.objects.filter(region_id=regionid,type_id=typeid)
        print("4")
    elif not namer and climater and not typer and regionr:
        pokemons = Pokemon.objects.filter(climate=climater,region_id=regionid)
        print("5")
    elif not namer and climater and typer and not regionr:
        pokemons = Pokemon.objects.filter(climate=climater,type_id=typeid)
        print("6")
    ################## ALL BUT NAME PROVIDED #############
    elif not namer and climater and typer and regionr:
        pokemons = Pokemon.objects.filter(climate=climater,region_id=regionid,type_id=typeid)
        print("7")
    ################## WITH NAME PROVIDED ################
    elif namer and not climater and not typer and regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,region_id=regionid)
        print("8")
    elif namer and not climater and typer and not regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,type_id=typeid)
        print("9")
    elif namer and climater and not typer and not regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,climate=climater)
        print("10")
    elif namer and not climater and typer and regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,region_id=regionid,type_id=typer)
        print("11")
    elif namer and climater and not typer and regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,climate=climater,region_id=regionid)
        print("12")
    elif namer and climater and typer and not regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,climate=climater,type_id=typer)
        print("13")
    ################### ALL PROVIDED ########################
    elif namer and climater and typer and regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer,region_id=regionid,climate=climater,type_id=typeid)
        print("14")
    elif namer and not climater and not typer and not regionr:
        pokemons = Pokemon.objects.filter(name__icontains=namer)
        print("15")
    else:
        pokemons = Pokemon.objects.order_by('number')
        print("16")

    #if len(Pokemon.objects.filter(name=namer,region_id=regionid,climate=climater,type_id=typeid)) == 0:

    if choice == "numberA":
        pokemons = pokemons.order_by('number')
    elif choice == "numberD":
        pokemons = pokemons.order_by('-number')
    elif choice == "nameA":
        pokemons = pokemons.order_by('name')
    elif choice == "nameD":
        pokemons = pokemons.order_by('-name')
    else:
        pokemons = pokemons
        
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})

def pokemon_collection(request):
    pokemons = Pokemon.objects.order_by('-number')
    return render(request, 'pokedex/pokemon_list.html', {'pokemons': pokemons})