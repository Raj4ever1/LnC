from features.auth.logout.logoutFeature import LogoutFeature
from userData import User


class Logout:
    __logoutFeature = None
    def __init__(self,services, userData:User):
        self.userData = userData
        self.__services = services

    @property
    def logoutFeature(self):
        if self.__logoutFeature is None:
            self.__logoutFeature = LogoutFeature(self.__services,self.userData)
        return self.__logoutFeature