from config_dataclass import ConfigData
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from datetime import datetime


class AuthLog:
    __current_client_host = None

    @staticmethod
    def do_log_auth(auth_status):
        with open(ConfigData.log_auth, "a") as f:
            now_human_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            f.write(f"AUTH:    {auth_status} IN {now_human_time}\n")

    def set_default_current_client_host(self):
        self.__current_client_host = None

    def log_attempt_new_connection_host(self, host):
        if host != self.__current_client_host:
            self.__current_client_host = host
            self.do_log_auth(f"SUCCESS FROM {host}")


security = HTTPBasic()
auth_logger = AuthLog()


def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = str.encode(ConfigData.user, encoding="utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = str.encode(ConfigData.password, encoding="utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    if not (is_correct_username and is_correct_password):
        auth_logger.do_log_auth(f"FAIL with creds {credentials.username}:{credentials.password}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
