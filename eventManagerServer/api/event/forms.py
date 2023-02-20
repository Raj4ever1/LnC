from django import forms

# import GeeksModel from models.py
from .models import Event, EventGameMap, EventUserMap


# create a ModelForm
class EventForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Event
        fields = '__all__'

class EventGameMapForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EventGameMap
        exclude = ('event_id',)

class EventUserMapForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EventUserMap
        exclude = ('event_id',)
