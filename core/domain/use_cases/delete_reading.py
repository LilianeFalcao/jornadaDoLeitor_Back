from typing import TypedDict

from ..repositories import IReadingsRepository


class DeleteReadingParams(TypedDict):
    """Define a estrutura dos parâmetros necessários para excluir uma leitura."""

    id_user: str
    id_manga: str


class DeleteReading:
    def __init__(self, reading_repository: IReadingsRepository):
        self.reading_repository = reading_repository

    async def execute(self, params: DeleteReadingParams) -> None:
        id_user = params["id_user"]
        id_manga = params["id_manga"]

        await self.reading_repository.delete(
            id_manga,
            id_user,
        )
