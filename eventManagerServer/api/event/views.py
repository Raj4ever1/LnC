import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse

from api.services import Service
from ..utills.database import DatabaseQuery,DatabaseQueryStringSelect
from ..utills.authentication import is_authenticated
from .models import Event
from .forms import EventForm, EventGameMapForm, EventUserMapForm


service = Service()
# Create your views here.
@api_view(['GET', 'POST'])
def events(request):
    method = request.method
    if not is_authenticated(request): 
        response = Response(status=status.HTTP_401_UNAUTHORIZED)
        return response
    if method == 'GET':
        includeEvents = request.GET.get('includeEvents','True').lower() == 'true'
        events = service.event_service.get_all_events(includeEvents)
        response = Response(data = json.loads(json.dumps(events, indent=4, sort_keys=True, default=str)))
        return response
    elif method == 'POST':
        received_json_data = json.loads(json.dumps(request.data))
        data,valid = service.event_service.create_event(received_json_data)
        if valid:
            return Response(json.loads(json.dumps(data, indent=4, sort_keys=True, default=str)))
        else:
            return Response(json.loads(json.dumps(data, indent=4, sort_keys=True, default=str)),status=status.HTTP_400_BAD_REQUEST)
        
    return Response(json.loads(json.dumps(request.method)))

@api_view(['GET'])
def event_details(request, event_id:int):
    if not is_authenticated(request): 
        response = Response(status=status.HTTP_401_UNAUTHORIZED)
        return response
    event = _get_event_details(event_id)
    if len(event) == 1:
        response = Response(data = json.loads(json.dumps(event, indent=4, sort_keys=True, default=str)))
    else:
        response = Response(status=status.HTTP_404_NOT_FOUND, data='Event with id: {} does not exists'.format(event_id))
    return response

def _get_event_details(event_id):
    db = DatabaseQuery()
    event = db.select(DatabaseQueryStringSelect.EVENT_USING_EVENT_ID, event_id)
    event[0]["managers"] = [element['user_id_id'] for element in db.select(DatabaseQueryStringSelect.MANAGERS_FOR_EVENT,event[0]["id"])]
    if len(event)>0:
        event[0]["games"] = db.select(DatabaseQueryStringSelect.GAMES_USING_EVENT_ID,event[0]["id"])
    return event