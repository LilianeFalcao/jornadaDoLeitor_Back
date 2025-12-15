from typing import List, TypedDict

from ..entity.reading import Readings, ReadingStatus
from ..repositories import IReadingsRepository


class ListReadingByStatusParams(TypedDict):
    """Define a estrutura dos parâmetros: requer um status de leitura."""

    status: ReadingStatus


class ListReadingByStatus:
    """
    Use Case para listar registros de leitura (Readings) com base em um status específico.
    """

    def __init__(self, reading_repository: IReadingsRepository):
        """
        Inicializa o Use Case com o repositório de leituras.
        """
        self.reading_repository = reading_repository

    async def execute(self, params: ListReadingByStatusParams) -> List[Readings]:
        """
        Busca leituras pelo status fornecido.

        Args:
            params: Dicionário contendo o status de leitura desejado.

        Returns:
            Uma lista de objetos Readings.

        Raises:
            ValueError: Se nenhuma leitura for encontrada com o status especificado.
        """
        status: ReadingStatus = params["status"]

        readings = await self.reading_repository.find_by_status(status)

        if not readings:
            raise ValueError(f"No readings found with status: {status.value}")

        return readings
