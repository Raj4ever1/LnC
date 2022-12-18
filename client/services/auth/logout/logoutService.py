from services.base.baseService import BaseService, BaseModel
from user_data import User


class LogoutModel(BaseModel):
    token: str

    def __init__(self, jsonData):
        self.token = jsonData["token"]


class LogoutService(BaseService):
    def __init__(self, user: User):
        url = 'auth/logout/'
        super().__init__(url=url, model=LogoutModel, user=user)
