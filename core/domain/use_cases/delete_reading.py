from core.domain.repositories import IReadingRepository
# Assumindo que a interface IReadingRepository está importada
# Nota: Você deve definir uma exceção de domínio mais específica (ex: ReadingNotFoundError)
# Mas usaremos ValueError, que é capturado pelo FastAPI.


class DeleteReading:
    """
    Use Case para deletar o registro de leitura de um mangá específico para um usuário.
    """

    def __init__(self, reading_repository: IReadingRepository):
        """
        Injeta o repositório de leitura.
        """
        self.reading_repository = reading_repository

    async def execute(self, id_user: str, id_manga: str) -> None:
        """
        Executa a lógica de deleção.

        Args:
            id_user: O ID do usuário logado.
            id_manga: O ID do mangá cuja leitura será deletada.

        Raises:
            ValueError: Se o registro de leitura não for encontrado.
        """

        reading = await self.reading_repository.find_by_user_and_manga(
            id_user=id_user, id_manga=id_manga
        )

        if not reading:
            # Lança um erro que será capturado pelo roteador (FastAPI)
            raise ValueError(
                f"Reading record not found for user '{id_user}' and manga '{id_manga}'."
            )

        # 2. Executa a deleção
        # O repositório realiza a operação no banco de dados
        await self.reading_repository.delete(id_manga=id_manga, id_user=id_user)
