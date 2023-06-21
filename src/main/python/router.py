from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import file_worker
from config_dataclass import ConfigData


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=ConfigData.front_path + "static"),
    name="static"
)

app.mount(
    "/pic",
    StaticFiles(directory=ConfigData.pictures_path),
    name="pic"
)

app.mount(
    "/vid",
    StaticFiles(directory=ConfigData.video_path),
    name="vid"
)

app.mount(
    "/mus",
    StaticFiles(directory=ConfigData.music_path),
    name="mus"
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
        "menus.html", {"request": request,
                       "title": "pictures",
                       "list": file_worker.get_dirs_in_path(ConfigData.pictures_path)}
    )


@app.get("/pictures/{directory}")
async def pictures_directory(request: Request, directory):
    files = file_worker.generate_json(directory, ConfigData.pictures_path)
    return templates.TemplateResponse(
        "pictures.html", {"request": request,
                          "directory": directory,
                          "title": "pictures",
                          "list": files,
                          }
    )


@app.get("/videos")
async def videos(request: Request):
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "videos",
                       "list": file_worker.get_dirs_in_path(ConfigData.video_path)
                       }
    )


@app.get("/videos/{directory}")
async def video_directory(request: Request, directory):
    files = file_worker.get_all_files_in_directory(directory, ConfigData.video_path)
    return templates.TemplateResponse(
        "videos.html", {"request": request,
                        "directory": directory,
                        "title": "videos",
                        "list": files}
    )


@app.get("/music")
async def music(request: Request):
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "music",
                       "list": file_worker.get_dirs_in_path(ConfigData.music_path)}
    )


@app.get("/music/{directory}")
async def music_directory(request: Request, directory):
    files = file_worker.generate_json(directory, ConfigData.music_path)
    return templates.TemplateResponse(
        "music.html", {"request": request,
                       "directory": directory,
                       "title": "music",
                       "list": files
                       }
    )
