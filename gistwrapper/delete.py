
from requests import delete
from json import dumps
from classes import GistItem

class DeleteGist:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, headers:dict):
        self.headers = headers

    def removeGist(self, gist_id: str) -> bool:
        header = self.headers

        resp = delete(f"{self.BASE_URL}/{gist_id}", headers=header)

        resp_code = resp.status_code

        return resp_code == 204
    

