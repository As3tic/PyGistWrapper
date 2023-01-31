from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class Token(BaseModel):
    gist_token: str

gist_token = ""

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def request_token(request: Request):
    return templates.TemplateResponse("token-accept.html", {"request": request})


@app.post("/set-token")
def set_token(token: Token):
    global gist_token # replace with session shenanigans and verify the token!
    gist_token = token.gist_token
    return 200

