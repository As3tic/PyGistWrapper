from typing import Dict
from os import getenv

from star import StarGist
from get_gist import GetGist
from fork import ForkGist
from create import CreateGist


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
        header: Dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.gist_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        self.headers = header


class Gist(GistBase):
    def __init__(self):
        super().__init__()
        self.load_modules()

    def load_modules(self) -> None:
        self.star = StarGist(self.headers)
        self.get = GetGist(self.headers)
        self.fork = ForkGist(self.headers)
        self.create = CreateGist(self.headers)


if __name__ == "__main__":
    gist = Gist()

    # TEST CREATE
    # files = {"README.md": {"content": "Hello World"}}
    # create_gist = gist.create.newGist(description="A sample readme file", public=False, files=files)

    # print(create_gist)

    # TEST FORK
    # forks = gist.fork.getForks(gist_id="54b4995bd68275691a23")
    # print(forks)

    # fork_gist = gist.fork.createFork(gist_id="2cd39deefde8c8926b1127c9029165ab")
    # print(fork_gist)

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
    # gist_commits = gist.get.commits(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_commits[0])
