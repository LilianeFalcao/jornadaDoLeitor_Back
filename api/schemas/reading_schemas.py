import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ReadingStatus(enum.StrEnum):
    READING = "reading"
    COMPLETED = "completed"


class ReadingCreate(BaseModel):
    id_manga: str
    start_date: datetime
    current_chapter: int
    progress: float = Field(
        default=0.0, ge=0.0, le=100.0, description="Progresso total (0.0 a 1.0)."
    )
    status: ReadingStatus = Field(
        default=ReadingStatus.READING, description="Status da leitura."
    )
    notes: Optional[str] = Field(default="", description="Anotações sobre a leitura.")


class ReadingUpdate(BaseModel):
    current_chapter: Optional[int] = Field(None, ge=0)
    progress: Optional[float] = Field(None, ge=0.0, le=1.0)
    status: Optional[ReadingStatus] = None
    notes: Optional[str] = None


class ReadingResponse(BaseModel):
    id: str
    id_user: str
    id_manga: str
    start_date: datetime
    current_chapter: int
    progress: float
    status: ReadingStatus
    notes: str

    model_config = ConfigDict(from_attributes=True)
