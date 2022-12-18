from features.auth import AuthFeature
from user_data import User


class Features:
    __auth = None
    def __init__(self, services, user_data:User):
        self.user_data = user_data
        self.__services = services

    @property
    def authFeature(self):
        if self.__auth is None:
            self.__auth = AuthFeature(self.__services, self.user_data)
        return self.__auth

