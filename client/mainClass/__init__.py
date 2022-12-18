from mainClass.featureMap import FeatureMap
from mainClass.main import Main
from user_data.user_data import UserData


class MainClass:
    __main = None
    __map = None
    def __init__(self,features,services):
        self.__features = features
        self.services = services

    @property
    def main(self):
        if self.__main is None:
            self.__main = Main(self.__features, self.services)
        return self.__main

    @property
    def map(self):
        if self.__map is None:
            self.__map = FeatureMap(self.__features)
        return self.__map
