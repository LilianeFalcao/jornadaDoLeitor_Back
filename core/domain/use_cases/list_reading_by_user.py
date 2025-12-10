from typing import List

# Importações assumidas com base na sua estrutura de projeto
from core.domain.entity import Reading
from core.domain.repositories import IReadingRepository


class ListUserReading:
    """
    Use Case para listar todos os registros de leitura de um usuário específico.
    """

    def __init__(self, reading_repository: IReadingRepository):
        # Injeção da dependência do repositório
        self.reading_repository = reading_repository

    async def execute(self, id_user: str) -> List[Reading]:
        """
        Busca e retorna a lista de leituras do usuário.

        Args:
            id_user: O ID do usuário cujas leituras devem ser listadas.

        Returns:
            Uma lista de entidades Reading.

        Raises:
            ValueError: Se nenhuma leitura for encontrada para o usuário.
        """

        # O método findByUserId foi traduzido para find_by_user_id (snake_case)
        readings = await self.reading_repository.find_by_user_id(id_user)

        # Verifica se a lista está vazia
        if not readings or len(readings) == 0:
            # Substituindo 'throw new Error' por 'raise ValueError' em Python
            raise ValueError("No readings found for this user")

        return readings
