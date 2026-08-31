import requests
from django.shortcuts import render

# Create your views here.

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

