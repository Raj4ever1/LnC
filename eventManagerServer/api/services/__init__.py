from .event import Event
from .team import Team

class Service:
    __event = None
    __team = None
    
    @property
    def event_service(self):
        if self.__event is None:
            __event = Event()
        return __event
    
    @property
    def team_service(self):
        if self.__team is None:
            __team = Team()
        return __team