from src.main.python.db.worker_db import get_user
from src.main.python.security.auth_log import AuthLog
from src.main.python.security.hash_data import hash_data

auth_logger = AuthLog()


def check_user_password(username: str, password: str) -> bool:
    users = get_user(username)
    for user in users:
        if user.password == hash_data(password):
            return True
        return False
