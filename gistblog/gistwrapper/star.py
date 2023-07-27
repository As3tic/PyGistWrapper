from requests import delete, get, put

class StarGist:
    BASE_URL = "https://api.github.com/gists"

    def __init__(self, headers:dict):
        self.headers = headers

    def checkIfStarred(self, gist_id: str) -> bool:
        resp = get(f"{self.BASE_URL}/{gist_id}/star", headers=self.headers)
        resp_code = resp.status_code

        print(resp_code)
        return resp_code == 204


    def add(self, gist_id: str) -> bool:
        resp = put(f"{self.BASE_URL}/{gist_id}/star", headers=self.headers)
        resp_code = resp.status_code

        print(resp_code)
        return resp_code == 204
    

    def unstar(self, gist_id: str) -> bool:
        resp = delete(f"{self.BASE_URL}/{gist_id}/star", headers=self.headers)
        resp_code = resp.status_code

        print(resp_code)
        return resp_code == 204