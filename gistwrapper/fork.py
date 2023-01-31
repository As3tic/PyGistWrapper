
from requests import delete, get, post
from classes import GistItem, GistCommit
from typing import List

class ForkGist:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, headers:dict):
        self.headers = headers

    def getForks(self, gist_id: str) -> List[GistItem]:
        resp = get(f"{self.BASE_URL}/{gist_id}/forks", headers=self.headers)

        gists = resp.json()


        gist_iterator = [GistItem(**g) for g in gists]

        return gist_iterator
    


    def createFork(self, gist_id: str) -> bool:
        resp = post(f"{self.BASE_URL}/{gist_id}/forks", headers=self.headers)
        resp_code = resp.status_code

        return resp_code == 201
