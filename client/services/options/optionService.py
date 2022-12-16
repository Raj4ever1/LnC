from services.base.baseService import BaseService, BaseModel
from userData import User


class OptionsModel(BaseModel):
    options = list[str]

    def __init__(self, jsonData):
        self.options = jsonData["options"]


class OptionsService(BaseService):
    def __init__(self, user: User):
        url = 'options'
        super().__init__(url=url, model=OptionsModel, user=user)
