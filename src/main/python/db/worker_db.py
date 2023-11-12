from os import path, remove
from datetime import datetime
from typing import Union
from sqlalchemy import func, desc, and_

from src.main.python.db.db import create_db, session, drop_db
from src.main.python.db.models import *

from src.main.python.config.config_dataclass import ConfigData
from src.main.python.security.hash_data import hash_data


def add_data(data):
    session.add(data)
    session.commit()


def _create_database():
    create_db()


def _drop_database():
    drop_db()


def init_database():
    # try:
    #     _drop_database()
    # except Exception as e:
    #     print(e)
    # finally:
    _create_database()
    add_user(ConfigData.user, hash_data(ConfigData.password), "admin", True)


def add_user(username, password, role, is_active):
    user = Users(username=username,
                 password=password,
                 role=role,
                 is_active=is_active)
    add_data(user)


def get_user(username) -> list:
    q = session.query(
        Users
    ).filter(
        Users.username == username
    ).all()

    return q
