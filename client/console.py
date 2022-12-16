from features import Features
from features.auth.login.loginFeature import LoginFeature
from mainClass import MainClass
from services import Services
from userData import User, UserData


class Console:
    def __init__(self):
        loginResponse = LoginFeature().login()
        if loginResponse.status == 200:
            userData = UserData(loginResponse.data['email'], loginResponse.data['first_name'],
                                loginResponse.data['last_name'], loginResponse.data['token'],
                                loginResponse.data['role'])
            self.userdata = User(userData)
            self.services = Services(self.userdata)
            self.features = Features(self.services, self.userdata)
            self.main = MainClass(self.features, self.services)
            self.main.main.startProcess()


if __name__ == '__main__':
    Console()
