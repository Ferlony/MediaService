from src.main.python.db.worker_db import get_user
from src.main.python.security.auth_log import AuthLog
from src.main.python.security.hash_data import hash_data

auth_logger = AuthLog()


def check_user(username: str, password: str):
    user = get_user(username)
    print(user)
    if not user:
        return False
    if __check_user_password(user, password) and __check_is_activated(user):
        return True
    return False


def __check_user_password(user, password: str) -> bool:
    if user.password == hash_data(password):
        return True
    return False


def __check_is_activated(user) -> bool:
    if user.is_active:
        return True
    return False
