from django.http import HttpResponse
import requests

def type1(request):
    response = requests.get("https://pokeapi.co/api/v2/type/1")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type2(request):
    response = requests.get("https://pokeapi.co/api/v2/type/2")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type3(request):
    response = requests.get("https://pokeapi.co/api/v2/type/3")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type4(request):
    response = requests.get("https://pokeapi.co/api/v2/type/4")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type5(request):
    response = requests.get("https://pokeapi.co/api/v2/type/5")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type6(request):
    response = requests.get("https://pokeapi.co/api/v2/type/6")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type7(request):
    response = requests.get("https://pokeapi.co/api/v2/type/7")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type8(request):
    response = requests.get("https://pokeapi.co/api/v2/type/8")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type9(request):
    response = requests.get("https://pokeapi.co/api/v2/type/9")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type10(request):
    response = requests.get("https://pokeapi.co/api/v2/type/10")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type11(request):
    response = requests.get("https://pokeapi.co/api/v2/type/11")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type12(request):
    response = requests.get("https://pokeapi.co/api/v2/type/12")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type13(request):
    response = requests.get("https://pokeapi.co/api/v2/type/13")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type14(request):
    response = requests.get("https://pokeapi.co/api/v2/type/14")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type15(request):
    response = requests.get("https://pokeapi.co/api/v2/type/15")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type16(request):
    response = requests.get("https://pokeapi.co/api/v2/type/16")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type17(request):
    response = requests.get("https://pokeapi.co/api/v2/type/17")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)


def type18(request):
    response = requests.get("https://pokeapi.co/api/v2/type/18")
    display = response.json()
    result = display["pokemon"]
    pokemons = ''
    for i in result:

        pokemons = pokemons + '<li>' + i['pokemon']['name'] + '</li>'

    return HttpResponse(pokemons)

