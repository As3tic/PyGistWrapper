from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from gistwrapper import Gist

from dotenv import load_dotenv
load_dotenv()

class Token(BaseModel):
    gist_token: str

client = Gist()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def request_token(request: Request):
    if client.gist_token == None:
        return templates.TemplateResponse("token-accept.html", {"request": request})
    return {
        "message":"Welcome"
    }


@app.post("/set-token")
def set_token(token: Token):
    client.set_token(token=token.gist_token)

    return 200


@app.get("/me")
def who_am_i(request: Request):
    identiy = client.get.Gist(category="")[0].author

    data = identiy.__dict__

    return templates.TemplateResponse("user-page.html", {"request": request, "user":data})
