from sqlalchemy import Column, String, Numeric
from .base import Base


class Manga(Base):
    __tablename__ = "mangas"

    id = Column(String, primary_key=True, index=True)
    img_URL = Column(String)
    title = Column(String)
    author_name = Column(String)
    gender = Column(String)
    total_chapters = Column(Numeric)
