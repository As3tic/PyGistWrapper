from typing import Dict, List
from requests import get, put
from classes import Gist, GistCommit
from os import getenv

class GistWrapper:
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

    def get_gists(self, category: str = "") -> List[Gist]:
        """Returns gists
        Category: str
         Can be either 'starred', 'public' or '' (for gists by the user)
        """
        header = self.headers
        header["per_page"] = "10"

        resp = get(f"{self.BASE_URL}/{category}", headers=header)

        gists = resp.json()

        gist_iterator = [Gist(**g) for g in gists]

        return gist_iterator
    

    def get_by_id(self, gist_id: str) -> Gist:
        resp = get(f"{self.BASE_URL}/{gist_id}", headers=self.headers)
        data = resp.json()

        return Gist(**data)
    
    def get_commits(self, gist_id: str) -> List[GistCommit]:
        resp = get(f"{self.BASE_URL}/{gist_id}/commits", headers=self.headers)
        data = resp.json()

        commits = [GistCommit(**data) for data in data]

        return commits


    def check_if_starred(self, gist_id: str) -> bool:
        resp = get(f"{self.BASE_URL}/{gist_id}/star", headers=self.headers)
        resp_code = resp.status_code

        print(resp_code)
        return resp_code == 204


    def star(self, gist_id: str) -> bool:
        resp = put(f"{self.BASE_URL}/{gist_id}/star", headers=self.headers)
        resp_code = resp.status_code

        print(resp_code)
        return resp_code == 204


if __name__ == "__main__":
    wrapper = GistWrapper()


    is_starred = wrapper.check_if_starred(gist_id="4582cb1902a626231c7a2746082f7ee4")
    print("IS Starred?", is_starred)

    star_gist = wrapper.star(gist_id="4582cb1902a626231c7a2746082f7ee4")
    print("Starred?", star_gist)

    is_starred = wrapper.check_if_starred(gist_id="4582cb1902a626231c7a2746082f7ee4")
    print("IS Starred?", is_starred)
    
    # gists = wrapper.get_gists(category="starred")
    # print(gists[0])

    # gist_by_id = wrapper.get_by_id(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_by_id)

    # gist_commits = wrapper.get_commits(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_commits[0])