from services.auth import Auth
from services.base import Base
from services.options import Options
from userData import User


class Services:
    __auth = None
    __base = None
    __options = None
    def __init__(self, user:User = None):
        self.__user = user

    @property
    def auth(self):
        if self.__auth is None:
            self.__auth = Auth(self.__user)
        return self.__auth

    @property
    def base(self):
        if self.__base is None:
            self.__base = Base(self.__user)
        return self.__base

    @property
    def options(self):
        if self.__options is None:
            self.__options = Options(self.__user)
        return self.__options
