from typing import List, Optional

from core.domain.entity import Reading
from core.domain.repositories import IReadingRepository
from core.domain.enum.reading_status import ReadingStatus


class MockReadingRepository(IReadingRepository):
    def __init__(self):
        self.readings: List[Reading] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ----------------------------------------------------------------------
    # Implementação dos Métodos da Interface (Assíncronos)
    # ----------------------------------------------------------------------

    async def save(self, reading: Reading) -> None:
        """Adiciona um novo registro de leitura à lista."""
        self.readings.append(reading)

    async def update(self, reading: Reading) -> Reading:
        """Atualiza um registro de leitura existente pelo ID."""
        # Encontra o índice do registro
        try:
            reading_index = next(
                i for i, r in enumerate(self.readings) if r.id == reading.id
            )
            # Atualiza o item na lista
            self.readings[reading_index] = reading
        except StopIteration:
            # Não encontrou o item (em um mock simples, podemos ignorar ou levantar um erro)
            pass

        return reading

    async def delete(self, id_manga: str, id_user: str) -> None:
        """Deleta o registro de leitura específico pelo ID do usuário e do mangá."""
        # Filtra a lista, mantendo apenas os registros que NÃO correspondem aos IDs
        self.readings = [
            reading
            for reading in self.readings
            if not (reading.id_user == id_user and reading.id_manga == id_manga)
        ]

    async def find_by_user_id(self, id_user: str) -> List[Reading]:
        """Busca todas as leituras de um usuário."""
        # Usa list comprehension para replicar .filter()
        return [reading for reading in self.readings if reading.id_user == id_user]

    async def find_by_status(self, status: ReadingStatus) -> List[Reading]:
        """Busca todas as leituras por status."""
        # Usa list comprehension para replicar .filter()
        return [reading for reading in self.readings if reading.status == status]

    async def find_by_user_and_manga(
        self, id_user: str, id_manga: str
    ) -> Optional[Reading]:
        """Busca uma leitura específica por usuário e mangá."""
        # Usa next() para replicar .find()
        return next(
            (
                r
                for r in self.readings
                if r.id_user == id_user and r.id_manga == id_manga
            ),
            None,
        )

    # ----------------------------------------------------------------------
    # Método Auxiliar
    # ----------------------------------------------------------------------

    def clear(self) -> None:
        """Limpa todos os dados mockados para testes."""
        self.readings = []
