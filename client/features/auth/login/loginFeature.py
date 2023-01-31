from services.auth.login.loginService import LoginService,LoginModel
from user_data import User, UserData


class LoginFeature:

    @staticmethod
    def login():
        email = input('Enter the email: ')#'ronak.jain11@intimetec.com'#
        password = input('Enter the password: ')#'17BTRCS118@'#
        return LoginService(User(UserData())).post(LoginModel({
            "email" : email,
            "password": password
        }))


