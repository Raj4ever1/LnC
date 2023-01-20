import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Option
from ..authentication.models import Role


# Create your views here.
def getOptions(request):
    response = HttpResponse()
    response.status_code = status.HTTP_200_OK
    try:
        role = Token.objects.get(key = request.headers['token']).user.role.pk
    except:
        role = 4
    options = []
    for option in Option.objects.filter(role = Role.objects.get(id = role)):
        options.append(option.option)
    response.content = json.dumps({
        'options': options+(['Notifications','Logout'] if role != 4 else ['Exit']),
    })
    response.content_type='application/json'
    return response
