from features.auth import AuthFeature
from userData import User


class Features:
    __auth = None
    def __init__(self, services, userData:User):
        self.userData = userData
        self.__services = services

    @property
    def authFeature(self):
        if self.__auth is None:
            self.__auth = AuthFeature(self.__services, self.userData)
        return self.__auth

