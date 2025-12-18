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

    async def execute(self, id_reading: str) -> None:
        await self.reading_repository.delete(id_reading=id_reading)
