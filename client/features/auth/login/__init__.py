from services.auth import LoginService


class Login:
    __login = None

    @property
    def login(self):
        if self.__login is None:
            self.__login = LoginService()
        return self.__login
