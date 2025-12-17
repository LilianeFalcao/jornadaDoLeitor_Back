from typing import List, Optional

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select as sql_select

# Assumindo estas importações em sua estrutura:
from core.domain.entity import Reading as ReadingEntity

# Importando o Enum definido no domínio para uso na interface
from core.domain.entity.reading import ReadingStatus
from core.domain.repositories import IReadingRepository
from core.infra.orm.reading import Reading as ReadingModel


class ReadingRepository(IReadingRepository):
    """
    Implementação do repositório para o domínio Reading usando SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    # --- Método Auxiliar de Conversão ---
    def _to_entity(self, model: ReadingModel) -> ReadingEntity:
        """Converte um modelo ORM em uma entidade de domínio."""
        return ReadingEntity(
            id=model.id,
            id_user=model.id_user,
            id_manga=model.id_manga,
            start_date=model.start_date,
            _current_chapter=model.current_chapter,
            _progress=model.progress,
            _status=ReadingStatus(model.status),
            _notes=model.notes,
        )

    # ----------------------------------------------------------------------
    # Implementação dos Métodos da Interface
    # ----------------------------------------------------------------------

    async def save(self, reading: ReadingEntity) -> None:
        """Cria um novo registro de leitura."""
        reading_model = ReadingModel(
            id=reading.id,
            id_user=reading.id_user,
            id_manga=reading.id_manga,
            start_date=reading.start_date,
            current_chapter=reading.current_chapter,
            progress=reading.progress,
            status=reading.status.value,
        )
        self.session.add(reading_model)
        await self.session.commit()

    async def update(self, reading: ReadingEntity) -> ReadingEntity:
        """Atualiza um registro de leitura existente. Usa a entidade como fonte."""

        result = await self.session.execute(
            sql_select(ReadingModel).where(ReadingModel.id == reading.id)
        )
        reading_model = result.scalar_one_or_none()

        if reading_model:
            reading_model.current_chapter = reading.current_chapter
            reading_model.progress = reading.progress
            reading_model.status = reading.status.value
            reading_model.notes = reading.notes

            await self.session.commit()
            return self._to_entity(reading_model)

        return reading

    async def delete(self, id_manga: str, id_user: str) -> None:
        """Deleta o registro de leitura específico."""
        await self.session.execute(
            delete(ReadingModel).where(
                ReadingModel.id_user == id_user, ReadingModel.id_manga == id_manga
            )
        )
        await self.session.commit()

    async def find_by_user_id(self, id_user: str) -> List[ReadingEntity]:
        """Busca todas as leituras de um usuário."""
        result = await self.session.execute(
            sql_select(ReadingModel).where(ReadingModel.id_user == id_user)
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def find_by_status(self, status: ReadingStatus) -> List[ReadingEntity]:
        """Busca todas as leituras por status."""

        # Filtra pelo valor string do Enum
        result = await self.session.execute(
            sql_select(ReadingModel).where(ReadingModel.status == status.value)
        )
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def find_by_user_and_manga(
        self, id_user: str, id_manga: str
    ) -> Optional[ReadingEntity]:
        """
        Busca uma leitura específica por ID de usuário e ID de mangá.

        Args:
            id_user: O ID do usuário.
            id_manga: O ID do mangá.

        Returns:
            ReadingEntity: O registro de leitura encontrado, ou None se não existir.
        """
        result = await self.session.execute(
            sql_select(ReadingModel).where(
                # Filtro 1: O ID do Usuário deve corresponder
                ReadingModel.id_user == id_user,
                # Filtro 2: O ID do Mangá deve corresponder
                ReadingModel.id_manga == id_manga,
            )
        )

        # 2. Executa e obtém o resultado
        # 'scalar_one_or_none()' garante que no máximo um objeto seja retornado.
        reading_model = result.scalar_one_or_none()

        # 3. Converte e retorna
        if reading_model:
            return self._to_entity(reading_model)

        return None  # Retorna None se nenhum registro for encontrado

    async def find_by_id_and_user(
        self, id_reading: str, id_user: str
    ) -> Optional[ReadingEntity]:
        """
        Busca um registro de leitura pelo ID do registro e ID do usuário
        (garante posse do recurso).
        """
        result = await self.session.execute(
            sql_select(ReadingModel).where(
                ReadingModel.id == id_reading,
                ReadingModel.id_user == id_user,
            )
        )

        reading_model = result.scalar_one_or_none()

        if reading_model:
            return self._to_entity(reading_model)

        return None
