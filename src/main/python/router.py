from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request


app = FastAPI()
front_path = "../resources/mediaservice/src/"

app.mount(
    "/static",
    StaticFiles(directory=front_path + "styles"),
    name="static",
)

templates = Jinja2Templates(directory=front_path + "templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
