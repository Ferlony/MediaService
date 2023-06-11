import asyncio
import uvicorn
from router import app
import configparser


async def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    config_host = str(config["DEFAULT"]["host"])
    config_port = int(config["DEFAULT"]["port"])

    config = uvicorn.Config("main:app", host=config_host, port=config_port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
