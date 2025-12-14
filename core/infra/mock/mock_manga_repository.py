from typing import List, Optional

from core.domain.entity import Manga
from core.domain.repositories import IMangaRepository


class MockMangaRepository(IMangaRepository):
    """
    Implementação Mock do repositório para testes, seguindo o padrão Singleton
    e usando métodos assíncronos.
    """

    def __init__(self):
        self.mangas: List[Manga] = []

    async def save(self, manga: Manga) -> None:
        """Adiciona um novo mangá à lista."""
        existing = await self.find_by_id(manga.id)
        if existing:
            # Se o mangá já existe, encontra o índice e o substitui
            try:
                index = self.mangas.index(existing)
                self.mangas[index] = manga
            except ValueError:
                # Deveria ser inatingível se find_by_id funcionar
                self.mangas.append(manga)
        else:
            # Caso contrário, adiciona o novo mangá
            self.mangas.append(manga)

    async def find_by_author_name(self, author_name: str) -> List[Manga]:
        """Busca mangás pelo nome do autor."""
        return [manga for manga in self.mangas if manga.author_name == author_name]

    async def find_by_id(self, id: str) -> Optional[Manga]:
        """Busca um mangá pelo ID, retornando None se não encontrado."""
        return next((manga for manga in self.mangas if manga.id == id), None)

    async def find_by_title(self, title: str) -> Optional[Manga]:
        """Busca um mangá pelo título, retornando None se não encontrado."""
        return next((manga for manga in self.mangas if manga.title == title), None)

    async def find_all(self) -> List[Manga]:
        """Retorna uma cópia da lista de todos os mangás."""
        return list(self.mangas)
