from services.base.baseService import BaseService, BaseModel


class SignupModel(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

    def __init__(self, jsonData):
        self.email = jsonData["email"]
        self.password = jsonData["password"]
        self.first_name = jsonData["first_name"]
        self.last_name = jsonData["last_name"]


class SignupService(BaseService):
    def __init__(self,user):
        url = 'auth/signup/'
        super().__init__(url=url, model=SignupModel, user=user)
