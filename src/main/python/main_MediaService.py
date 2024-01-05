import os.path
from threading import Thread, Timer

import asyncio
# from hypercorn.config import Config
# from hypercorn.asyncio import serve
import uvicorn

from src.main.python.router import app
from src.main.python.config.config_dataclass import ConfigData
from src.main.python.security.security import auth_logger
from src.main.python.file_worker import clear_tmp, check_tmp_structure


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


async def main():
    if not os.path.exists(ConfigData.log_auth):
        open(ConfigData.log_auth, "w")

    check_tmp_structure()

    config = uvicorn.Config("src.main.python.main_MediaService:app",
                            host=ConfigData.config_host,
                            port=ConfigData.config_port,
                            log_level="info")

    server = uvicorn.Server(config)
    await server.serve()

    # config = Config()
    # config.from_toml("hypercorn_config.toml")
    #
    # await serve(app, config)


if __name__ == "__main__":

    timer1 = RepeatTimer(ConfigData.timer, auth_logger.set_default_current_client_host)
    timer1.start()

    timer2 = RepeatTimer(ConfigData.timer, clear_tmp)
    timer2.start()

    server_th = Thread(target=asyncio.run(main()))
    server_th.start()
