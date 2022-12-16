from features.auth.login import Login
from features.auth.logout import Logout
from userData import User


class AuthFeature:
    __login = None
    __signup = None
    __logout = None
    def __init__(self,services, userData:User):
        self.userData = userData
        self.__services = services

    @property
    def login(self):
        if self.__login is None:
            self.__login = Login()
        return self.__login

    @property
    def logout(self):
        if self.__logout is None:
            self.__logout = Logout(self.__services,self.userData)
        return self.__logout