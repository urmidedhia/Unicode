from django.http import HttpResponse
import requests


def types(request):
    response = requests.get("https://pokeapi.co/api/v2/type/")
    display = response.json()
    result = display["results"]
    poketypes = ''
    for i in result:
        poketypes = poketypes + '<li>' + i['name'] + '</li>'
    return HttpResponse(poketypes)
