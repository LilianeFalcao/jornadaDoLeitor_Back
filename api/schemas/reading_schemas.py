from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from core.domain.enum.reading_status import ReadingStatus


class ReadingCreate(BaseModel):
    id_manga: str
    start_date: datetime
    current_chapter: int
    notes: Optional[str] = Field(default="", description="Notes on the reading.")


class ReadingUpdate(BaseModel):
    current_chapter: Optional[int] = Field(None, ge=0)
    notes: Optional[str] = None


class ReadingResponse(BaseModel):
    id: str
    id_user: str
    id_manga: str
    start_date: datetime
    current_chapter: int
    progress: float
    status: ReadingStatus
    notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
