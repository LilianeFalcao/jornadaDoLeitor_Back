from pydantic import BaseModel, Field
from typing import Optional


class MangaCreate(BaseModel):
    img_URL: str
    title: str
    author_name: str
    gender: str
    total_chapters: int


class MangaUpdate(BaseModel):
    img_URL: Optional[str] = None
    title: Optional[str] = None
    author_name: Optional[str] = None
    gender: Optional[str] = None
    total_chapters: Optional[int] = Field(None, ge=0)


class MangaResponse(BaseModel):
    id: str
    img_URL: str
    title: str
    author_name: str
    gender: str
    total_chapters: int

    class Config:
        from_attributes = True
