from features import Features
from features.auth.login.loginFeature import LoginFeature
from mainClass import MainClass
from services import Services
from user_data import User, UserData


class Console:
    def __init__(self):
        login_response = LoginFeature().login()
        user_data = UserData()
        if login_response.status == 200:
            user_data = UserData(login_response.data['email'], login_response.data['first_name'],
                                login_response.data['last_name'], login_response.data['token'],
                                login_response.data['role'])
        self.user_data = User(user_data)
        self.services = Services(self.user_data)
        self.features = Features(self.services, self.user_data)
        self.main = MainClass(self.features, self.services)
        self.main.main.startProcess()


if __name__ == '__main__':
    Console()
