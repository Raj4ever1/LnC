from userData.userData import UserData


class User:
    __userData = None
    def __init__(self, userData = UserData()):
        self.__userData = userData

    @property
    def userData(self):
        return self.__userData

