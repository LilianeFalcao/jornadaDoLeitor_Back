from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies import get_use_case_factory
from api.schemas.manga_schemas import MangaCreate, MangaResponse
from core.factories.use_case_factory import UseCaseFactory

mangas_router = APIRouter()


# ------------------
# Adicionar Mangas
# -----------------
@mangas_router.post("/mangas")
async def create_mangas(
    manga_data: MangaCreate, factory: UseCaseFactory = Depends(get_use_case_factory)
):
    try:
        add_manga_use_case = factory.create_add_mangas()
        created_manga = await add_manga_use_case.execute(
            img_URL=manga_data.img_URL,
            title=manga_data.title,
            author_name=manga_data.author_name,
            gender=manga_data.gender,
            total_chapters=manga_data.total_chapters,
        )
        return MangaResponse(
            id=created_manga.id,
            img_URL=created_manga.img_URL,
            title=created_manga.title,
            author_name=created_manga.author_name,
            gender=created_manga.gender,
            total_chapters=created_manga.total_chapters,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
