from services import Services
from services.auth.logout.logoutService import LogoutModel
from user_data import User


class LogoutFeature:
    def __init__(self, services:Services, user_data:User):
        self.user_data = user_data
        self.services = services

    def logout(self):
        return self.services.auth.logout.post(LogoutModel({
            "token": self.user_data.user_data.token
        }))


