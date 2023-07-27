
from requests import delete, get, put
from typing import List
from gistblog.gistwrapper.classes import GistItem, GistCommit

class GetGist:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, headers:dict):
        self.headers = headers

    def Gist(self, category: str = "") -> List[GistItem]:
        """Returns gists
        Category: str
         Can be either 'starred', 'public' or '' (for gists by the user)
        """
        header = self.headers
        header["per_page"] = "10"

        if category == "":
            resp = get(self.BASE_URL, headers=header)
        else:
            resp = get(f"{self.BASE_URL}/{category}", headers=header)

        gists = resp.json()

        gist_iterator = [GistItem(**g) for g in gists]

        return gist_iterator
    

    def ById(self, gist_id: str) -> GistItem:
        resp = get(f"{self.BASE_URL}/{gist_id}", headers=self.headers)
        data = resp.json()

        return GistItem(**data)
    
    def Commits(self, gist_id: str) -> List[GistCommit]:
        resp = get(f"{self.BASE_URL}/{gist_id}/commits", headers=self.headers)
        data = resp.json()

        commits = [GistCommit(**data) for data in data]

        return commits