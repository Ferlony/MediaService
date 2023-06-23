import asyncio
import uvicorn
from router import app
from config_dataclass import ConfigData
import os.path
from threading import Timer
from security import auth_logger


async def main():
    if not os.path.exists(ConfigData.log_auth):
        open(ConfigData.log_auth, "w")

    Timer(ConfigData.timer, auth_logger.set_default_current_client_host)

    config = uvicorn.Config("main:app", host=ConfigData.config_host, port=ConfigData.config_port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
