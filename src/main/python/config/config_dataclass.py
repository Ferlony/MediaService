import configparser
from dataclasses import dataclass

from src.main.python.gen_def import read_json


@dataclass
class ConfigData:
    front_path = "./src/main/resources/mediaservice/"
    db_path = "./src/main/python/local/db.sqlite3"

    log_auth = f"src/main/python/log/auth.log"

    config = configparser.ConfigParser()
    config.read("src/main/python/config/config.ini")
    config_host = str(config["DEFAULT"]["host"])
    config_port = int(config["DEFAULT"]["port"])
    timer = float(config["DEFAULT"]["timer"])

    pictures_path = str(config["FILES"]["pictures"])
    video_path = str(config["FILES"]["video"])
    music_path = str(config["FILES"]["music"])
    text_path = str(config["FILES"]["text"])
    
    config_host_torrents = str(config["TORRENTS"]["host"])
    config_port_torrents = str(config["TORRENTS"]["port"])

    user = str(config["SECRETS"]["user"])
    password = str(config["SECRETS"]["password"])

    secret: str = config["SECRETS"]["secret"]
    algorithm: str = config["SECRETS"]["algorithm"]

    date_format = "%Y-%m-%d %H:%M:%S"

    allowed_formats = read_json("src/main/python/config/allowed_formats.json")
    allowed_img = allowed_formats["img"]
    allowed_video = allowed_formats["video"]
    allowed_music = allowed_formats["music"]
