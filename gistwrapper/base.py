from typing import Dict, List
from requests import delete, get, put
from classes import GistItem, GistCommit
from os import getenv

from star import StarGist
from get_gist import GetGist

class GistBase:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, token=None):
        if token is None:
            from dotenv import load_dotenv

            load_dotenv()
            self.gist_token = getenv("GIST_TOKEN")
        else:
            self.gist_token = token

        self.generate_headers()


    def generate_headers(self) -> None:
        header: Dict[str, str] ={
            "Accept": "application/vnd.github+json",
            "Authorization" : f"Bearer {self.gist_token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        self.headers = header

class Gist(GistBase):

    def __init__(self):
        super().__init__()
        self.load_modules()

    def load_modules(self) -> None:
        self.star = StarGist(self.headers)
        self.get = GetGist(self.headers)


if __name__ == "__main__":
    gist = Gist()

    # TEST STAR
    # status = gist.star.check_if_starred(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # status = gist.star.star(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # status = gist.star.unstar(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # TEST FETCH GISTS    
    # gists = gist.get.gists(category="")
    # print(gists[0])

    # gist_by_id = gist.get.by_id(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_by_id)

    # TEST GET COMMITS
    gist_commits = gist.get.commits(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    print(gist_commits[0])