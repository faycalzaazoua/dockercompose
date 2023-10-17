from fastapi import FastAPI, Request
from os import environ as env
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# def index():
#     return { "message": f"Hello {env['MY_VARIABLE']} !"}
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "my_variable": env['name']})


# def second_route():
#     return { "message": "Ceci est la deuxième route."}
@app.get("/second-route")
def index(request: Request):
    return templates.TemplateResponse("annexe.html", {"request": request})
