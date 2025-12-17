# Arquivo: core/domain/use_cases/find_reading_by_id_and_user.py

from typing import Optional
from core.domain.entity import Reading as ReadingEntity
from core.domain.repositories import IReadingRepository


class FindReadingByIdAndUser:
    """
    Use Case para buscar um registro de leitura específico pelo ID do Registro
    e o ID do Usuário para garantir que a leitura pertence ao usuário logado.
    """

    def __init__(self, reading_repository: IReadingRepository):
        self.reading_repository = reading_repository

    async def execute(self, id_reading: str, id_user: str) -> Optional[ReadingEntity]:
        """
        Busca uma leitura por seu ID e o ID do usuário.

        Args:
            id_reading: O ID único do registro de leitura (e.g., UUID).
            id_user: O ID do usuário logado (para posse).

        Returns:
            O registro de leitura ou None.
        """

        # O repositório precisará de um novo método: find_by_id_and_user
        reading = await self.reading_repository.find_by_id_and_user(
            id_reading=id_reading, id_user=id_user
        )

        return reading
