import json

from django.http import JsonResponse
from django.shortcuts import render

from people.models import People
from swapi.api import get_people_by_id

def get_by_id(request, id):
    try:
        person = People.objects.get(pk=id)
    except People.DoesNotExist as dne:
        success, response = get_people_by_id(id)
        person = People(
            person_id=id,
            name=response['name'],
            height=int(response['height']),
            mass=int(response['mass']),
            hair_color=response['hair_color'],
            eye_color=response['eye_color'],
            birth_year=response['birth_year'],
            gender=response['gender'],
        )
        person.save()
    
    return JsonResponse(person.to_json(), status=200)