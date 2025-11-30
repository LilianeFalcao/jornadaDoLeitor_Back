from abc import ABC, abstractmethod
from typing import Optional, List

from ..entity.reading import Reading


class Readings:
    pass


class ReadingStatus:
    pass


class IReadingRepository(ABC):
    @abstractmethod
    async def save(self, reading: Readings) -> None:
        """Salva um novo registro de leitura."""
        pass

    @abstractmethod
    async def update(self, reading: Readings) -> Readings:
        """Atualiza um registro de leitura existente e o retorna."""
        pass

    @abstractmethod
    async def delete(self, id_manga: str, id_user: str) -> None:
        """Deleta um registro de leitura com base no ID do mangá e do usuário."""
        pass

    @abstractmethod
    async def find_by_user_id(self, id_user: str) -> List[Readings]:
        """Busca todos os registros de leitura de um usuário específico."""
        pass

    @abstractmethod
    async def find_by_status(self, status: ReadingStatus) -> List[Readings]:
        """Busca todos os registros de leitura com um determinado status."""
        pass

    @abstractmethod
    async def find_by_user_and_manga(
        self, id_user: str, id_manga: str
    ) -> Optional[Readings]:
        """Busca um registro de leitura específico por ID do usuário e ID do mangá."""
        pass
