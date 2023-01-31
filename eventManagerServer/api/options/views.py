import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token

from api.utills.database import DatabaseQueryStringSelect, DatabaseQuery
 
from .models import Option
from ..authentication.models import Role, UserRoleMap
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def getOptions_restApi(request):
    db = DatabaseQuery()
    try:
        user = Token.objects.get(key = request.headers['token']).user.pk
    except:
        user = None
    result = db.select(DatabaseQueryStringSelect.OPTIONS_USING_USER_ID if user else DatabaseQueryStringSelect.OPTIONS_USING_ROLE_ID, user if user else 4)
    result.append({
                "option": "Notification",
                "function_key": "555"
            })
    result.append({
                "option": "Logout",
                "function_key": "666"
            }
    )
    return Response(json.loads(json.dumps(result)))

