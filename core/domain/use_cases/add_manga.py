import uuid

# Importações assumidas com base na sua estrutura de projeto
from core.domain.entity import Manga
from core.domain.repositories import IMangaRepository


class AddManga:
    """
    Use Case para adicionar um novo mangá ao catálogo.
    """

    def __init__(self, manga_repository: IMangaRepository):
        # Injeção da dependência do repositório de mangás
        self.manga_repository = manga_repository

    async def execute(
        self,
        img_URL: str,
        title: str,
        author_name: str,
        gender: str,
        total_chapters: int,
    ) -> Manga:
        """
        Cria e salva uma nova entidade Manga.

        Raises:
            ValueError: Se o mangá já existir (opcional, dependendo da regra de negócio).
        """

        new_manga = Manga(
            id=str(uuid.uuid4()),
            img_URL=img_URL,
            title=title,
            author_name=author_name,
            gender=gender,
            total_chapters=total_chapters,
        )

        await self.manga_repository.save(new_manga)

        return new_manga
