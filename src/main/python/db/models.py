from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey, Boolean,
    JSON
    )

# from sqlalchemy.orm import relationship

from src.main.python.db.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)

    register_date = Column(DateTime)
    previous_auth = Column(DateTime)
    sync_data = Column(JSON)

    is_active = Column(Boolean)

    def __init__(self, username, password, role, register_date, previous_auth, sync_data, is_active):
        self.username = username
        self.password = password
        self.role = role
        self.register_date = register_date
        self.previous_auth = previous_auth
        self.sync_data = sync_data
        self.is_active = is_active

    def __repr__(self):
        info: str = f"id: {self.id}, username: {self.username},"\
                    f"role: {self.role}, register_date: {self.register_date},"\
                    f"previous_auth: {self.previous_auth},"\
                    f"sync_data: {self.sync_data}, is_active: {self.is_active}"
        return info
