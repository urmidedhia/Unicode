from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')


def types(request):
    type = request.GET.get('text', 'default')
    type = type.lower()
    response = requests.get("https://pokeapi.co/api/v2/type/")
    display = response.json()
    result = display["results"]

    pokemons = ''
    for i in result:
        if i['name'] == type:
            response = requests.get(i['url'])
            display = response.json()
            result = display["pokemon"]
            for j in result:
                pokemons = pokemons + '<li>' + j['pokemon']['name'] + '</li>'

    if pokemons != '':
        return HttpResponse(pokemons)
    else:
        return HttpResponse("Error! Invalid Input")


