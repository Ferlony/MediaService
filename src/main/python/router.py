from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()
front_path = "../resources/mediaservice/src/"


@app.get("/")
async def get_index():
    return FileResponse(front_path + "index.html")
