from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    nickname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
