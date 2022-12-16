from services.auth.signup.signupService import SignupService,SignupModel
fileData = open('../../../assets/features/signup/signup.csv', 'r').read().split('\n')
columns = fileData[0].split(',')
users = fileData[1:]
validColumns = ['email', 'password', 'first_name', 'last_name']

for user in users:
    data = {}
    for index in range(len(columns)):
        data[columns[index]] = user.split(',')[index]
    payload = SignupModel(data)
    response = SignupService().post(payload)
    print(response.status, user.split(',')[0])
