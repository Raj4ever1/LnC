from services.options.optionService import OptionsService
from userData import User


class Options:
    __options = None

    def __init__(self, userData:User):
        self.userData = userData

    @property
    def options(self):
        if self.__options is None:
            self.__options = OptionsService(self.userData)
        return self.__options
