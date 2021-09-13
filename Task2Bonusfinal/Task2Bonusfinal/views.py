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

def berries(request):
    response = requests.get("https://pokeapi.co/api/v2/berry?offset=0&limit=64")
    display = response.json()
    results = display["results"]
    berries = ""

    for i in results:
        berries = berries + '<li>' + i["name"]

    return HttpResponse(berries)

def homepage(request):
    display = '''Hello, welcome to the world of pokemons...<ol>
<li>type /pokemons in the url to get a list of all pokemons
<li>type /berries in the url to get a list of all berries
    </ol>'''
    return HttpResponse(display)
