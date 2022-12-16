import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Option


# Create your views here.
def getOptions(request):
    response = HttpResponse()
    response.status_code = status.HTTP_200_OK
    user = Token.objects.get(key = request.headers['token']).user
    options = []
    for option in Option.objects.filter(role = user.role):
        options.append(option.option)
    response.content = json.dumps({
        'options': options+(['Notifications','Logout'] if user.role.pk != 4 else ['Logout']),
    })
    response.content_type='application/json'
    return response
