from features import Features


class  FeatureMap:
    def __init__(self, features:Features):
        self.features = features

    @property
    def map(self):
        return {
            '666': self.features.authFeature.logout.logoutFeature.logout,
            '11': self.features.authFeature.signup.signupFeatrue.bulk_signup,
        }