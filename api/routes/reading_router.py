from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
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


# ------------------
# Buscar Leitura
# -----------------

@readings_router.get("/readings", response_model=List[ReadingResponse])
async def get_readings(
    factory: UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user)
):
    try:
        list_user_reading_use_case = factory.create_list_reading_by_user()
        readings = await list_user_reading_use_case.execute(id_user=current_user.id) # EXECUTE precisa de um ID
        return readings
    except ValueError as e:
        # 404 Not Found se não houver leituras para o usuário
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
# --- Fim da Correção do GET ---

@readings_router.put("/readings/{id_manga}", response_model=ReadingResponse)
async def update_readings(
    id_manga: str,
    reading_data: ReadingUpdate,
    factory:  UseCaseFactory = Depends(get_use_case_factory),
    current_user: User = Depends(get_current_user),
):
    try:
        update_reading_use_case = factory.create_update_reading()
        # 2. Executa o Use Case
        # O Use Case precisa: ID do usuário (logado), ID do mangá (URL), novo capítulo (corpo)
        updated_reading = await update_reading_use_case.execute(
            id_user=current_user.id,
            id_manga=id_manga,
            new_current_chapter=reading_data.new_current_chapter,
            # NOTA: O Use Case UpdateReading deve ser modificado para buscar total_chapters internamente.
        )
        return updated_reading
    except ValueError as e:
        # Trata "Registro de leitura não encontrado" ou validações de capítulo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        # Erro genérico do servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal error while updating reading.")