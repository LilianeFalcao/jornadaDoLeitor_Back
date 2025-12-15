from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.domain.entity import Manga as MangaEntity
from core.domain.repositories import IMangaRepository
from core.infra.orm.manga import Manga as MangaModel


class MangaRepository(IMangaRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_entity(self, model: MangaModel) -> MangaEntity:
        """Converte um objeto MangaModel do ORM para uma entidade de domínio MangaEntity."""
        return MangaEntity(
            id=model.id,
            img_URL=model.img_URL,
            title=model.title,
            author_name=model.author_name,
            gender=model.gender,
            total_chapters=model.total_chapters,
        )

    async def save(self, manga: MangaEntity) -> None:
        manga_model = MangaModel(
            id=manga.id,
            img_URL=manga.img_URL,
            title=manga.title,
            author_name=manga.author_name,
            gender=manga.gender,
            total_chapters=manga.total_chapters,
        )
        self.session.add(manga_model)
        await self.session.commit()

    async def find_by_author_name(self, author_name: str) -> List[MangaEntity]:
        """Busca mangás pelo nome do autor."""
        result = await self.session.execute(
            select(MangaModel).where(MangaModel.author_name == author_name)
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def find_by_id(self, id: str) -> Optional[MangaEntity]:
        """Busca um mangá pelo ID."""
        result = await self.session.execute(
            select(MangaModel).where(MangaModel.id == id)
        )
        manga_model = result.scalar_one_or_none()

        if manga_model:
            return self._to_entity(manga_model)
        return None

    async def find_by_title(self, title: str) -> Optional[MangaEntity]:
        """Busca um mangá pelo título."""
        result = await self.session.execute(
            select(MangaModel).where(MangaModel.title == title)
        )
        manga_model = result.scalar_one_or_none()

        if manga_model:
            return self._to_entity(manga_model)
        return None

    async def find_all(self) -> List[MangaEntity]:
        """Retorna todos os mangás."""
        result = await self.session.execute(select(MangaModel))
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]
