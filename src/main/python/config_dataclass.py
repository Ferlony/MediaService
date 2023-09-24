import configparser
from dataclasses import dataclass


@dataclass
class ConfigData:
    front_path = "../resources/mediaservice/"
    log_auth = "auth.log"

    config = configparser.ConfigParser()
    config.read("config.ini")
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
