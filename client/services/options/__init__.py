from services.options.optionService import OptionsService
from user_data import User


class Options:
    __options = None

    def __init__(self, user_data:User):
        self.user_data = user_data

    @property
    def options(self):
        if self.__options is None:
            self.__options = OptionsService(self.user_data)
        return self.__options
