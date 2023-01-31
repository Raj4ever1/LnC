from services.base.baseService import BaseService, BaseModel
from user_data import User

class OptionModel(BaseModel):
    options = str
    feature_key = str
    def __init__(self, jsonData):
        self.option = jsonData["option"]
        self.feature_key = jsonData['function_key']
class OptionsModel(BaseModel):
    options:list[OptionModel]

    def __init__(self, jsonData):
        self.options = []
        for option in jsonData:
            self.options.append(OptionModel(option))


class OptionsService(BaseService):
    def __init__(self, user: User):
        url = 'options/'
        super().__init__(url=url, model=OptionsModel, user=user)
