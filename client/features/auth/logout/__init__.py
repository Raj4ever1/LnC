from features.auth.logout.logoutFeature import LogoutFeature
from user_data import User


class Logout:
    __logoutFeature = None
    def __init__(self,services, user_data:User):
        self.user_data = user_data
        self.__services = services

    @property
    def logoutFeature(self):
        if self.__logoutFeature is None:
            self.__logoutFeature = LogoutFeature(self.__services,self.user_data)
        return self.__logoutFeature