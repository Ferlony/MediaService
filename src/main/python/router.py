from os import stat

from typing import Annotated, Optional
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import (FastAPI, Request, Depends, Header)
from starlette.responses import (RedirectResponse)

from src.main.python.security.auth_bearer import JWTBearer
from src.main.python.security.security import auth_logger, check_user_password
# from src.main.python.security.basic_http_auth import get_current_username
from src.main.python.security.auth_handler import signJWT

import src.main.python.file_worker as file_worker
from src.main.python.config.config_dataclass import ConfigData
from src.main.python.models import ParserModel, UserSchema
from src.main.python.media_response import MediaResponse


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=ConfigData.front_path + "src/" + "static"),
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

app.mount(
    "/node_modules",
    StaticFiles(directory=ConfigData.front_path + "src/" + "templates/" + "js/" + "node_modules"),
    name="node_modules"
)

templates = Jinja2Templates(directory=ConfigData.front_path + "src/" + "templates")


# Index
# @app.get("/")
# async def root(request: Request, username: Annotated[str, Depends(get_current_username)]):
#     auth_logger.log_attempt_new_connection_host(request.client.host)
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "username": username}
#     )
@app.get("/")
async def root(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/register")
async def register(request: Request):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "register.html", {"request": request}
    )    


# @app.post("/register")
# async def post_register(request: Request, item: UserSchema):
#     # TODO register db call
#
#     return signJWT(item.username)


@app.get("/login")
async def login(request: Request):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "login.html", {"request": request}
    )    


@app.post("/login")
async def post_login(request: Request, item: UserSchema):
    if check_user_password(item.username, item.password):
        return signJWT(item.username)
    return {"error": "Incorrect user or password"}


# Pictures
@app.get("/pictures")
async def pictures(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "pictures",
                       "img_prev": "pic",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.pictures_path)}
    )


@app.get("/pictures/{directory}")
async def pictures_directory(request: Request, directory, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.pictures_path, True, 1)
    return templates.TemplateResponse(
        "pictures.html", {"request": request,
                          "directory": directory,
                          "title": "pictures",
                          "list": files
                          }
    )


# Videos
@app.get("/videos")
async def videos(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "videos",
                       "img_prev": "vid",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.video_path)
                       }
    )


@app.get("/videos/{directory}")
async def video_directory(request: Request, directory, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.video_path, True)
    response = templates.TemplateResponse(
        "videos.html", {"request": request,
                        "directory": directory,
                        "title": "videos",
                        "list": files})
    # response.headers["Accept-Ranges"] = "bytes"
    return response


@app.get("/media_vid/{file_dir}/{file_path}")
async def media(file_dir: str, file_path: str, range_header: Optional[str] = Header('bytes=0-', alias="Range"),
                dependencies=[Depends(JWTBearer())]):
    print(file_path)

    if '..' in file_path:
        raise Exception(file_path + ' is not allowed')

    full_path = ConfigData.video_path + file_dir + "/" + file_path
    start, end = range_header.strip('bytes=').split('-')
    start = int(start)
    size = stat(full_path)[6]
    end = min(size-1, start+10)
    return MediaResponse(path=full_path, status_code=206, offset=start, headers={
        'Accept-Ranges': 'bytes',
        'Content-Range': 'bytes %s-%s/%s' % (start, end, size),
        'Content-Length': str(size-start)
    })


# Music
@app.get("/music")
async def music(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "music",
                       "img_prev": "mus",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.music_path)}
    )


@app.get("/music/{directory}")
async def music_directory(request: Request, directory, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.music_path, True)
    return templates.TemplateResponse(
        "music.html", {"request": request,
                       "directory": directory,
                       "title": "music",
                       "list": files
                       }
    )


# Text Files
@app.get("/textfiles")
async def textfiles(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "menus.html", {"request": request,
                       "title": "textfiles",
                       "img_prev": "text",
                       "list": file_worker.get_dirs_in_path_with_image(ConfigData.text_path)}
    )


@app.get("/textfiles/{directory}")
async def textfiles_directory(request: Request, directory, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    files = file_worker.get_files_in_directory(directory, ConfigData.text_path, True, 1)
    return templates.TemplateResponse(
        "text.html", {"request": request,
                          "directory": directory,
                          "title": "textfiles",
                          "list": files
                      }
    )


# Torrents
@app.get("/torrents", response_class=RedirectResponse)
async def torrents(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return RedirectResponse("http://" + ConfigData.config_host_torrents + ":" + ConfigData.config_port_torrents + "/transmission/web/")


# Parsers
@app.get("/parsers")
async def parsers(request: Request, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return templates.TemplateResponse(
        "parsers.html", {"request": request,
                         "title": "parsers"}
    )


@app.post("/parsers")
async def parsers_post(request: Request, item: ParserModel, dependencies=[Depends(JWTBearer())]):
    auth_logger.log_attempt_new_connection_host(request.client.host)
    return file_worker.define_parser(dict(item))
