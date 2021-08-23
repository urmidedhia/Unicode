from django.http import HttpResponse
import requests

def pokemons(request):
    '''response = requests.get("https://pokeapi.co/api/v2/pokemon")
    display = response.json()
    while display["next"] != "null":
        display = response.json()
        results = display["results"]
        pokemons = ""

        for i in results:
            pokemons = pokemons + '<li>' + i["name"]
        response = requests.get(display["next"])
    return HttpResponse(response)'''

    response = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=1118")
    display = response.json()
    results = display["results"]
    pokemons = ""

    for i in results:
        pokemons = pokemons + '<li>' + i["name"]

    return HttpResponse(pokemons)

