from fastapi import APIRouter, Depends, HTTPException, status
from api.dependencies import get_use_case_factory, get_current_user
from api.schemas.manga_schemas import (
    MangaCreate,
    MangaResponse
)
from core.factories.use_case_factory import UseCaseFactory
from core.domain.entity import Manga

mangas_router = APIRouter()

# ------------------
# Adicionar Mangas
# -----------------
@mangas_router.post("/mangas")
async def create_mangas(
    manga_data: MangaCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory)
):
    try:
        add_manga_use_case = factory.create_add_mangas()
        created_manga = await add_manga_use_case.execute(
            img_url=manga_data.img_URL,
            title=manga_data.title,
            author_name = manga_data.author_name,
            gender = manga_data.gender,
            total_chapters=manga_data.total_chapters,
        )
        return created_manga
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise hex(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))