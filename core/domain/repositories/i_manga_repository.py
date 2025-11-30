from abc import ABC, abstractmethod
from typing import Optional, List

from ..entity.manga import Manga


class IMangaRepository(ABC):
    @abstractmethod
    async def save(self, manga: Manga) -> None:
        """Salva um novo mangá ou atualiza um existente."""
        pass

    @abstractmethod
    async def find_by_author_name(self, author_name: str) -> List[Manga]:
        """Busca uma lista de mangás pelo nome do autor."""
        pass

    @abstractmethod
    async def find_by_title(self, title: str) -> Optional[Manga]:
        """Busca um mangá pelo título."""
        pass

    @abstractmethod
    async def find_by_id(self, id: str) -> Optional[Manga]:
        """Busca um mangá pelo seu ID único."""
        pass

    @abstractmethod
    async def find_all(self) -> List[Manga]:
        """Retorna uma lista contendo todos os mangás."""
        pass
