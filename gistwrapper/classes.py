from typing import Dict
from dateutil.parser import parse
from datetime import datetime


class GistSkeleton:
    
    def __repr__(self):
        pretty_obj: str = ""

        for key, value in self.__dict__.items():
            if type(value) in [str, int, bool, datetime]:
                pretty_obj += f"\n\t[{key.title()}] {value}\n"
            else:
                if type(value) == list:
                    for item in value:
                        pretty_obj += f"\t[{key.title()}]\n"

                        for key, value in item.__dict__.items():
                            pretty_obj += f"\t\t[{key.title()}] {value}\n"
                else:
                    pretty_obj += f"\t[{key.title()}]\n"

                    for key, value in value.__dict__.items():
                        pretty_obj += f"\t\t[{key.title()}] {value}\n"
                    
        return pretty_obj

class GistItem(GistSkeleton):
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

        user = kwargs.get("owner", {})

        self.url = f"https://gist.github.com/{user.get('login')}/{self.id}"

        self.author = GistAuthor(**user)

        self.public = kwargs.get("public")

        created_at = kwargs.get("created_at", "2000-02-02T13:00:00-02:00")
        self.created_at: datetime = parse(created_at)

        updated_at = kwargs.get("updated_at", "2000-02-02T13:00:00-02:00")
        self.updated_at: datetime = parse(updated_at)
        
        self.description = kwargs.get("description")
        self.comments = kwargs.get("comments")
        
        files: Dict = kwargs.get("files", {})

        self.files  = [GistFile(**fdata) for _fname, fdata in files.items()]

    

class GistFile(GistSkeleton):
    def __init__(self, **kwargs):
        self.filename = kwargs.get("filename")
        self.language = kwargs.get("language")
        self.url = kwargs.get("raw_url")
        self.size = kwargs.get("size")


class GistAuthor(GistSkeleton):
    def __init__(self, **kwargs):

        self.username = kwargs.get("login")
        self.avatar_url = kwargs.get("avatar_url", "")[:-4]
        self.profile_url = kwargs.get("html_url")
        self.followers = kwargs.get("followers_url")
        self.following = kwargs.get("following_url", "")[:-13]
        self.gists = kwargs.get("gists_url", "")[:-10]
        self.starred = kwargs.get("starred_url", "")[:-15]
        self.repos = kwargs.get("repos_url")
        

class GistCommit(GistSkeleton):
    def __init__(self, **kwargs):
        user = kwargs.get("user", {})

        self.author = GistAuthor(**user)

        changes = kwargs.get("change_status", {})
        self.deletions = changes["deletions"]
        self.additions = changes["additions"]
        self.total = changes["total"]
        
        updated_at = changes.get("committed_at", "2000-02-02T13:00:00-02:00")
        self.committed_at: datetime = parse(updated_at)
    