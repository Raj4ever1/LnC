from services.base.baseService import BaseService
from user_data import User


class Base:
    __base = None
    def __init__(self, user:User):
        self.__user = user

    @property
    def base(self):
        if self.__base is None:
            self.__base = BaseService(self.__user)
        return self.__base