from requests import delete, get, post
from gistwrapper.classes import User
from typing import List

class GetUser:
    BASE_URL = "https://api.github.com/users"

    def __init__(self, headers:dict):
        self.headers = headers

    def GetUsers(self) -> List[User]:
        resp = get(f"{self.BASE_URL}", headers=self.headers)
        data = resp.json()

        users = [User(**user) for user in data]
        return users

    def GetUser(self, user: str) -> User:
        resp = get(f"{self.BASE_URL}/{user}", headers=self.headers)
        data = resp.json()

        return User(**data)
    

