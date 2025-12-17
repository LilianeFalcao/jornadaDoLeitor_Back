from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.domain.enum.reading_status import ReadingStatus
from sqlalchemy import Enum

from .base import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(String, primary_key=True, index=True)
    id_user = Column(String, ForeignKey("users.id"))
    id_manga = Column(String, ForeignKey("mangas.id"))
    start_date = Column(DateTime)
    current_chapter = Column(Integer)
    progress = Column(Float(asdecimal=False))
    status = Column(
        Enum(ReadingStatus, name="reading_status", native_enum=True),
        nullable=False,
        default=ReadingStatus.READING,
    )
    notes = Column(String)

    user = relationship("User")
    manga = relationship("Manga", back_populates="readings")
