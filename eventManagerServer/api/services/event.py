from api.event.forms import EventForm, EventGameMapForm
from api.utills.database import DatabaseQuery, DatabaseQueryStringSelect


class Event:
    def __init__(self):
        self.db = DatabaseQuery()
        
    def create_event(self, event_body: dict):
        form = EventForm(event_body)
        game_is_valid = all([EventGameMapForm(game).is_valid() for game in event_body['games']])
        managers = event_body["managers"]
        list_of_managers = self.db.select(DatabaseQueryStringSelect.LIST_OF_MANAGERS)
        manager_is_valid = all([({'user_id_id': manager} in list_of_managers) for manager in managers])
        if form.is_valid() and len(event_body['games']) > 0 and game_is_valid\
            and len(managers) > 0 and manager_is_valid:
            event = event_body.copy()
            del event['games']
            del event['managers']
            event = self.db.insert('event_event',event)
            for game in event_body['games']:
                game["event_id_id"] = event["id"]
                game["game_id_id"] = game["game_id"]
                del game["game_id"]
                self.db.insert('event_eventgamemap',game)
            for manager in managers:
                self.db.insert('event_eventusermap',{"user_id_id": manager, "event_id_id":event["id"]})
            return self.get_event_details(event["id"]), True
        else:
            return form.errors, False
        
    def get_event_details(self, event_id):
        event = self.db.select(DatabaseQueryStringSelect.EVENT_USING_EVENT_ID, event_id)
        event[0]["managers"] = [element['user_id_id'] for element in self.db.select(DatabaseQueryStringSelect.MANAGERS_FOR_EVENT,event[0]["id"])]
        if len(event)>0:
            event[0]["games"] = self.db.select(DatabaseQueryStringSelect.GAMES_USING_EVENT_ID,event[0]["id"])
        return event
    
    def get_all_events(self, includeEvents):
        events = self.db.select(DatabaseQueryStringSelect.ALL_EVENTS)
        response_data = {
            "event_ids" : [event['id'] for event in events],
            "total": len(events)
        }
        if includeEvents:
            response_data['events'] = [self.get_event_details(event["id"])[0] for event in events]
        return response_data