from typing import Optional

# Importando a Entidade e a Interface do Repositório
from core.domain.entity import Reading as ReadingEntity
from core.domain.repositories import IReadingRepository


class FindReadingByUserAndManga:
    """
    Use Case para buscar um registro de leitura específico
    pelo ID do Usuário e o ID do Mangá.
    """

    def __init__(self, reading_repository: IReadingRepository):
        """
        Injeta a dependência do repositório de leituras.
        """
        self.reading_repository = reading_repository

    async def execute(self, id_user: str, id_manga: str) -> Optional[ReadingEntity]:
        """
        Executa a busca.

        Args:
            id_user: O ID do usuário que possui a leitura.
            id_manga: O ID do mangá associado à leitura.

        Returns:
            Optional[ReadingEntity]: O registro de leitura, se encontrado, ou None.
        """

        # O Use Case simplesmente delega a responsabilidade de busca ao Repositório
        reading = await self.reading_repository.find_by_user_and_manga(
            id_user=id_user, id_manga=id_manga
        )

        return reading

        # NOTA: Se você quisesse que este Use Case sempre falhasse se a leitura não existisse,
        # você adicionaria uma verificação aqui:
        # if not reading:
        #     raise ValueError("Reading record not found.")
        # Mas o retorno de Optional[ReadingEntity] é mais flexível para consultas.
