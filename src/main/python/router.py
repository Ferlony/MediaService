from typing import Annotated

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi import Depends
from starlette.responses import RedirectResponse

from security import get_current_username
from security import auth_logger
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

app.mount(
    "/text",
    StaticFiles(directory=ConfigData.text_path),
    name="text"
)

templates = Jinja2Templates(directory=ConfigData.front_path + "templates")


@app.get("/")
async def root(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "index.html", {"request": request, "username": username}
    )


@app.get("/pictures")
async def pictures(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "pictures",
                       "img_prev": "pic",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.pictures_path), "username": username}
    )


@app.get("/pictures/{directory}")
async def pictures_directory(request: Request, directory, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.pictures_path, True, 1)
    return templates.TemplateResponse(
        "pictures.html", {"request": request,
                          "directory": directory,
                          "title": "pictures",
                          "list": files, "username": username
                          }
    )


@app.get("/videos")
async def videos(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "videos",
                       "img_prev": "vid",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.video_path), "username": username
                       }
    )


@app.get("/videos/{directory}")
async def video_directory(request: Request, directory, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.video_path, True)
    return templates.TemplateResponse(
        "videos.html", {"request": request,
                        "directory": directory,
                        "title": "videos",
                        "list": files, "username": username}
    )


@app.get("/music")
async def music(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "music",
                       "img_prev": "mus",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.music_path), "username": username}
    )


@app.get("/music/{directory}")
async def music_directory(request: Request, directory, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.music_path, True)
    return templates.TemplateResponse(
        "music.html", {"request": request,
                       "directory": directory,
                       "title": "music",
                       "list": files, "username": username
                       }
    )

@app.get("/textfiles")
async def textfiles(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "textfiles",
                       "img_prev": "text",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.text_path), "username": username}
    )


@app.get("/textfiles/{directory}")
async def textfiles_directory(request: Request, directory, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.text_path, True, 1)
    return templates.TemplateResponse(
        "text.html", {"request": request,
                          "directory": directory,
                          "title": "textfiles",
                          "list": files, "username": username
                          }
    )

@app.get("/torrents", response_class=RedirectResponse)
async def torrents(request: Request, username: Annotated[str, Depends(get_current_username)]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return RedirectResponse("http://" + ConfigData.config_host_torrents + ":" + ConfigData.config_port_torrents + "/transmission/web/")

