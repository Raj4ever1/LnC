from services import Services
from services.auth.logout.logoutService import LogoutModel
from userData import User


class LogoutFeature:
    def __init__(self, services:Services, userData:User):
        self.userData = userData
        self.services = services

    def logout(self):
        return self.services.auth.logout.post(LogoutModel({
            "token": self.userData.userData.token
        }))


