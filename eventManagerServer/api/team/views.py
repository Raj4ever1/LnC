import json
from django.shortcuts import render
from api.services import Service
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
service = Service()

@api_view(['POST'])
def get_teams(request):
    data, valid = service.team_service.create_team(json.loads(json.dumps(request.data)))
    return Response(json.loads(json.dumps(data, indent=4, sort_keys=True, default=str)))