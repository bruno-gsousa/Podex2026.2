import requests
from django import forms 
from django.shortcuts import get_object_or_404, redirect, render

from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields =["name","species","height","weight","types","abilities","image"]
        widgets ={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "species": forms.TextInput(attrs={"class": "form-control"}),
            "height": forms.NumberInput(attrs={"class": "form-control","step":"0.1","min":"0"}),
            "weight": forms.NumberInput(attrs={"class": "form-control","step":"0.1","min":"0"}),
            "types": forms.TextInput(attrs={"class": "form-control"}),
            "abilities":forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.URLInput(attrs={"class": "form-control"}),
        }

def _serialize_db_pokemon(pokemon):
    types = [value.strip().title() for value in pokemon.types.split(",") if value.strip()]
    abilities = [value.strip().title() for value in pokemon.abilities.split(",") if value.strip()]
#continuar proxima aula

def _serialize_api_pokemon(details):
    types = [item["type"]["name"].title() for item in details.get("types",[])]
    abilites = [item["ability"]["name"].replace("-"," ").title() for item in details.get("abilities",[])]
    image = details.get("sprites",{}).get("other", {}).get("official-artwork",{}).get("front_default")
    if not image:
        image = details.get("sprites",{}.get("front_default"))

    return{
        "id": details.get("id"),
        "name": details.get("name", "").title(),
        "species":details.get("species",{}).get("name", "").title(),
        "height": f"{details.get('height',0)/10:1f} m",
        "weight": f"{details.get('weight',0)/10:1f} kg",
        "types": types,
        "abilities": abilites,
        "image": image,
        "source": "api",
    }

def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20'
    response = requests.get(url)
    dados = response.json()
    pokemons = []
    for pokemon in dados['results']:
        response_pokemon = requests.get(pokemon["url"])
        detalhes = response_pokemon.json()
        pokemons.append(_serialize_api_pokemon(detalhes))
       
    return render(request, 'index.html',{"pokemon":pokemons})

