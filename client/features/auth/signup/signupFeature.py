from services.auth.signup.signupService import SignupService,SignupModel

class SignupFeature:
    def __init__(self,services,user_data) -> None:
        self.user_data = user_data
        self.services = services
        
    def bulk_signup(self):
        fileData = open('assets/features/signup/signup.csv', 'r').read().split('\n')
        columns = fileData[0].split(',')
        users = fileData[1:]
        call_response = []
        for user in users:
            data = {}
            for index in range(len(columns)):
                data[columns[index]] = user.split(',')[index]
            payload = SignupModel(data)
            response = SignupService(self.user_data).post(payload)
            print(response.status, user.split(',')[0])
            call_response.append([response.status, user.split(',')[0]])
        return call_response