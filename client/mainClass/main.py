from features import Features
from services import Services
from mainClass.featureMap import FeatureMap


class Main:
    def __init__(self, features: Features, services: Services):
        self.services = services
        self.features = features
        self.featureMap = FeatureMap(self.features)

    def logout(self):
        return self.features.authFeature.logout.logoutFeature.logout()

    def startProcess(self):
        choice = None
        userOptions = self.services.options.options.get().data.options
        while choice != len(userOptions):
            print("*" * 30)
            for index in range(len(userOptions)):
                print(f'{index + 1}. {userOptions[index]}')
            choice = input('Enter your choice: ')
            if choice.isnumeric() and 0 < int(choice) <= len(userOptions):
                option = (str(self.services.options.user_data.user_data.role) + choice)
                choice = int(choice)
                if option in self.featureMap.map.keys():
                    self.featureMap.map[option]()
                else:
                    print('Feature code::{}. Feature yet to be implemented::{}'.format(option,userOptions[int(choice)-1]))

