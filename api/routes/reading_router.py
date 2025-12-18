from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies import get_current_user, get_use_case_factory
from api.schemas.reading_schemas import (
    ReadingCreate,
    ReadingResponse,
    ReadingUpdate,
)
from core.domain.entity import User
from core.factories.use_case_factory import UseCaseFactory

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


# ------------------
# Buscar Leitura
# -----------------


@readings_router.get("/readings", response_model=List[ReadingResponse])
async def get_readings(
    factory: UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user),
):
    try:
        list_user_reading_use_case = factory.create_list_reading_by_user()
        readings = await list_user_reading_use_case.execute(id_user=current_user.id)
        return readings
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


# ------------------
# Atualisar Leitura
# -----------------


@readings_router.put("/readings/{id_manga}", response_model=ReadingResponse)
async def update_readings(
    id_manga: str,
    reading_data: ReadingUpdate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user),
):
    try:
        update_reading_use_case = factory.create_update_reading()
        updated_reading = await update_reading_use_case.execute(
            id_user=current_user.id,
            id_manga=id_manga,
            current_chapter=reading_data.current_chapter,
            notes=reading_data.notes,
        )
        return updated_reading
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


# ------------------
# Deletar Leitura
# -----------------
@readings_router.delete(
    "/readings/{id_reading}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_reading(
    id_reading: str,  # Mudamos de id_manga para id_reading
    factory: UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user),
):
    try:
        reading = await factory.reading_repository.find_by_id_and_user(
            id_reading=id_reading, id_user=current_user.id
        )
        if reading is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Read log not found!"
            )

        if reading.id_user != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to delete this reading!",
            )

        delete_use_case = factory.create_delete_reading()
        await delete_use_case.execute(id_reading=id_reading)

        return

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
