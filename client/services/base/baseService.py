import json
import os
import socket

import requests
from requests import Response

from user_data import User


# class for response body
class responseBody:
    def __init__(self, response, model):
        self.status = response.status_code
        self.data = model
        self.headers = response.headers
        self.cookies = response.cookies


# Base Model Class
class BaseModel:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# Base Service Class
class BaseService:
    def __init__(self, url: str, model: any, user:User):
        self.url = url
        self.model = model
        self.host = f'http://{socket.gethostbyname(socket.gethostname())}:8000'
        self.token = user.user_data.token


    def _getHeaders(self):
        headers = {}
        if self.token is not None:
            headers = {
                "Token": self.token
            }
        return headers

    def get(self, argument: str = None):

        response = requests.get(self._getFullURL(argument), headers=self._getHeaders())
        return self._formResponseBody(response)

    def _getFullURL(self, argument=None):
        url = os.path.join(self.host, self.url)
        if argument:
            url = os.path.join(url, argument)
        return url.replace('\\', '/')

    def _formResponseBody(self, response):
        if response.status_code == 200:
            return responseBody(response, self.model(json.loads(response.content.decode())))
        else:
            return responseBody(response, None)

    def post(self, requestBody: any):
        if type(requestBody) == self.model:
            response = requests.post(self._getFullURL(), data=requestBody.toJSON(), headers=self._getHeaders())
            return responseBody(response, json.loads(response.content.decode()) if response.content else '')
        else:
            response = Response()
            response.status_code = 400
            return self._formResponseBody(response)
