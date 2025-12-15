from typing import List

# Importações assumidas com base na sua estrutura de projeto
from core.domain.entity import Manga  # O nome da sua entidade
from core.domain.repositories import IMangaRepository


class FindAllMangas:
    """
    Use Case para listar todos os registros de mangás disponíveis no sistema.
    """

    def __init__(self, mangas_repository: IMangaRepository):
        # Injeção da dependência do repositório
        self.mangas_repository = mangas_repository

    async def execute(self) -> List[Manga]:
        """
        Busca e retorna a lista de todos os mangás.
        """

        # O método findAll foi traduzido para find_all (snake_case)
        return await self.mangas_repository.find_all()
