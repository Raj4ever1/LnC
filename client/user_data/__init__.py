from user_data.user_data import UserData


class User:
    __user_data = None
    def __init__(self, user_data = UserData()):
        self.__user_data = user_data

    @property
    def user_data(self):
        return self.__user_data

