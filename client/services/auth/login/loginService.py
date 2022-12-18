from services.base.baseService import BaseService, BaseModel
from user_data import User


class LoginModel(BaseModel):
    email: str
    password: str

    def __init__(self, jsonData):
        self.email = jsonData["email"]
        self.password = jsonData["password"]


class LoginService(BaseService):
    def __init__(self,user: User):
        url = 'auth/login/'
        super().__init__(url=url, model=LoginModel, user= user)
