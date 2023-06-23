import configparser
from dataclasses import dataclass


@dataclass
class ConfigData:
    front_path = "../resources/mediaservice/src/"
    log_auth = "auth.log"

    config = configparser.ConfigParser()
    config.read("config.ini")
    config_host = str(config["DEFAULT"]["host"])
    config_port = int(config["DEFAULT"]["port"])
    timer = int(config["DEFAULT"]["timer"])

    pictures_path = str(config["FILES"]["pictures"])
    video_path = str(config["FILES"]["video"])
    music_path = str(config["FILES"]["music"])

    user = str(config["SECRETS"]["user"])
    password = str(config["SECRETS"]["password"])
