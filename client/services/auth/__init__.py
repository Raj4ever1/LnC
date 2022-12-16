from services.auth.login.loginService import LoginService
from services.auth.logout.logoutService import LogoutService
from services.auth.signup.signupService import SignupService
from userData import User


class Auth:
    __login = None
    __logout = None
    __signup = None
    def __init__(self, user:User):
        self.__user = user

    @property
    def login(self):
        if self.__login is None:
            self.__login = LoginService(self.__user)
        return self.__login

    @property
    def logout(self):
        if self.__logout is None:
            self.__logout = LogoutService(self.__user)
        return self.__logout

    @property
    def signup(self):
        if self.__signup is None:
            self.__signup = SignupService(self.__user)
        return self.__signup