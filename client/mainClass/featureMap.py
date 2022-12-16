from features import Features


class  FeatureMap:
    def __init__(self, features:Features):
        self.features = features

    @property
    def map(self):
        return {
            '44':self.features.authFeature.logout.logoutFeature.logout,
            '35':self.features.authFeature.logout.logoutFeature.logout
        }