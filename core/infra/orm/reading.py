from sqlalchemy import Column, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .base import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(String, primary_key=True, index=True)
    id_user = Column(String, ForeignKey("users.id"))
    id_manga = Column(String, ForeignKey("mangas.id"))
    start_date = Column(DateTime)
    current_chapter = Column(Numeric)
    progress = Column(Numeric)
    notes = Column(String)

    user = relationship("User")
    manga = relationship("Manga", back_populates="readings")
