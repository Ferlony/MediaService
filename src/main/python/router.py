from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import file_worker
from config_dataclass import ConfigData


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=ConfigData.front_path + "styles"),
    name="static",
)

templates = Jinja2Templates(directory=ConfigData.front_path + "templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/pictures")
async def pictures(request: Request):
    return templates.TemplateResponse(
        "pictures/pictures.html", {"request": request}
    )


@app.get("/videos")
async def pictures(request: Request):
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "videos",
                       "list": file_worker.get_dirs_in_path(ConfigData.video_path)
                       }
    )


@app.get("/videos/{directory}")
async def video_dir(request: Request, directory):
    files = file_worker.get_all_files_in_directory(directory, ConfigData.video_path)
    return templates.TemplateResponse(
        "music.html", {"request": request,
                       "directory": directory,
                       "title": "music",
                       "list": files}
    )


@app.get("/music")
async def pictures(request: Request):
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "music",
                       "list": file_worker.get_dirs_in_path(ConfigData.music_path)}
    )


@app.get("/music/{directory}")
async def music_playlist(request: Request, directory):
    files = file_worker.get_all_files_in_directory(directory, ConfigData.music_path)
    return templates.TemplateResponse(
        "music.html", {"request": request,
                       "directory": directory,
                       "title": "music",
                       "list": files}
    )
