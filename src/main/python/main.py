import asyncio
import uvicorn
from router import app
from config_dataclass import ConfigData
import os.path
from security import auth_logger
from threading import Thread, Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


async def main():
    if not os.path.exists(ConfigData.log_auth):
        open(ConfigData.log_auth, "w")

    config = uvicorn.Config("main:app", host=ConfigData.config_host, port=ConfigData.config_port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":

    timer = RepeatTimer(ConfigData.timer, auth_logger.set_default_current_client_host)
    timer.start()

    server_th = Thread(target=asyncio.run(main()))
    server_th.start()
