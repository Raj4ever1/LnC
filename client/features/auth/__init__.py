from features.auth.signup import Signup
from features.auth.login import Login
from features.auth.logout import Logout
from user_data import User


class AuthFeature:
    __login = None
    __signup = None
    __logout = None
    def __init__(self,services, user_data:User):
        self.user_data = user_data
        self.__services = services

    @property
    def login(self):
        if self.__login is None:
            self.__login = Login()
        return self.__login

    @property
    def logout(self):
        if self.__logout is None:
            self.__logout = Logout(self.__services,self.user_data)
        return self.__logout
    
    @property
    def signup(self):
        if self.__signup is None:
            self.__signup = Signup(self.__services, self.user_data)
        return self.__signup