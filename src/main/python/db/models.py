from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey, Boolean
    )

# from sqlalchemy.orm import relationship

from src.main.python.db.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)
    is_active = Column(Boolean)

    def __init__(self, username, password, role, is_active):
        self.username = username
        self.password = password
        self.role = role
        self.is_active = is_active

    def __repr__(self):
        info: str = f"id: {self.id}, username: {self.username},"\
                    f"role: {self.role}, is_active: {self.is_active}"
        return info
