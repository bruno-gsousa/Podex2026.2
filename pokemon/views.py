import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20'
    response = requests.get(url)
    dados = response.json()
    pokemons = []
    for pokemon in dados['results']:
        response_pokemon = requests.get(pokemon["url"])
        detalhes = response_pokemon.json()
        pokemons.append(detalhes)
       
    return render(request, 'index.html',{"pokemon":pokemons})

