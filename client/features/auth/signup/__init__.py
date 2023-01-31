from features.auth.signup.signupFeature import SignupFeature


class Signup:
    __signup = None

    def __init__(self, services, user_data) -> None:
        self.__services = services
        self.user_data = user_data

    @property
    def signupFeatrue(self):
        if self.__signup is None:
            self.__signup = SignupFeature(self.__services, self.user_data)
        return self.__signup
