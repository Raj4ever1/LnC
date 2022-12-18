from services.auth.login.loginService import LoginService,LoginModel
from user_data import User, UserData


class LoginFeature:

    @staticmethod
    def login():
        email = 'ronak.jain11@intimetec.com'#input('Enter the email: ')
        password = '17BTRCS118@'#input('Enter the password: ')
        return LoginService(User(UserData())).post(LoginModel({
            "email" : email,
            "password": password
        }))


