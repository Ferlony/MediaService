from os import path, remove
from datetime import datetime
from typing import Union

from sqlalchemy import func, desc, and_

from src.main.python.db.db import create_db, session, drop_db
from src.main.python.db.models import *

from src.main.python.config.config_dataclass import ConfigData
from src.main.python.security.hash_data import hash_data
from src.main.python.file_worker import get_now_time


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
    reg_date = get_now_time()
    add_user(ConfigData.user, hash_data(ConfigData.password), "admin", reg_date, None, None, True)


def add_user(username, password, role, register_date, previous_auth, sync_data, is_active):
    user = Users(username=username,
                 password=password,
                 role=role,
                 register_date=register_date,
                 previous_auth=previous_auth,
                 sync_data=sync_data,
                 is_active=is_active)
    if len(get_user(username)) > 0:
        raise Exception("User already exist")
    add_data(user)


def get_user(username: str):
    q = session.query(
        Users
    ).filter(
        Users.username == username
    ).all()

    for user in q:
        return user


def get_user_last_auth(username: str) -> datetime:
    q = session.query(
        Users.previous_auth
    ).filter(
        Users.username == username
    ).one()

    return q.previous_auth


def get_sync_data(username: str) -> Union[dict, None]:
    q = session.query(
        Users.sync_data
    ).filter(
        Users.username == username
    ).one()

    return q.sync_data


def update_sync_data(username: str, sync_data: dict) -> None:
    q = session.query(
        Users
    ).filter(
        Users.username == username
    ).update(
        {"sync_data": sync_data},
        synchronize_session='fetch'
    )
    session.commit()


def update_user_last_auth(username: str, current_auth: datetime) -> None:
    q = session.query(
        Users
    ).filter(
        Users.username == username
    ).update(
        {"previous_auth": current_auth},
        synchronize_session='fetch'
    )
    session.commit()
