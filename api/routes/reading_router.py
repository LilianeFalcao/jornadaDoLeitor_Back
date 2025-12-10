from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_use_case_factory, get_current_user
from api.schemas.reading_schemas import (
    ReadingCreate,
    ReadingResponse,
    ReadingUpdate,
)
from core.factories.use_case_factory import UseCaseFactory
from core.domain.entity import Reading, ReadingStatus, User


readings_router = APIRouter()


# ------------------
# Adicionar Leitura
# -----------------
@readings_router.post("/readings")
async def create_reading(
    reading_data: ReadingCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user),
):
    try:
        add_reading_use_case = factory.create_add_reading()
        created_reading = await add_reading_use_case.execute(
            id_user=current_user.id,
            id_manga=reading_data.id_manga,
            current_chapter=reading_data.current_chapter,
            notes=reading_data.notes,
        )
        return created_reading

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
