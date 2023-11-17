import time
from typing import Dict

import jwt

from src.main.python.config.config_dataclass import ConfigData


JWT_SECRET = ConfigData.secret
JWT_ALGORITHM = ConfigData.algorithm


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(username: str) -> Dict[str, str]:
    payload = {
        "username": username
        # "role": role
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        # return decoded_token if decoded_token["expires"] >= time.time() else None
        return decoded_token
    except:
        return {}
