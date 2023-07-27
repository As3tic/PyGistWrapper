from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from starlette.responses import RedirectResponse

from gistblog.gistwrapper import Gist

from dotenv import load_dotenv
load_dotenv()

client = Gist()

    

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# # redirect if token is not set
# @app.middleware("http")
# async def verify_user_agent(request: Request, call_next):
#     if request.method == "GET" and client.gist_token == None:
#         if request.url.path != "/get-token":
#                 url = app.url_path_for("get_token")
#                 response = RedirectResponse(url=url)
#                 return response
#         else:
#             response = await call_next(request)
#             return response
#     else:
#         response = await call_next(request)
#         return response

@app.get("/get-token")
def get_token(request: Request):
    return templates.TemplateResponse("token-accept.html", {"request": request})

@app.get("/")
def request_token(request: Request):
    url = app.url_path_for("me")
    response = RedirectResponse(url=url)
    return response


@app.post("/set-token")
def set_token(gist_token: str = Form()):
    client.set_token(token=gist_token)
    url = app.url_path_for("me")
    response = RedirectResponse(url=url)
    return response

@app.get("/me")
@app.post("/me")
def me(request: Request):
    data = client.get.Gist(category="")[0].author

    client.identity = data.__dict__

    return templates.TemplateResponse("user-page.html", {"request": request, "user":client.identity})


@app.get("/list")
def gist_list(request: Request, category: str = ""):
    """Get a list of gists

    Args:
        request (Request): _description_
        category (str, optional): Category of the Gist. Can be starred, public or gists created by user(''). Defaults to "".

    Returns:
        _type_: _description_
    """
    if category.lower() not in ["starred", "public", ""]: # allowed category list
        category = ""
    gist_list = client.get.Gist(category=category)
    
    return templates.TemplateResponse("gist-list.html", {"request": request, "gist_list": gist_list})
