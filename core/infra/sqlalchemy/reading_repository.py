from typing import List, Optional
from enum import Enum

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select as sql_select

# Assumindo estas importações em sua estrutura:
from core.domain.entity import Reading as ReadingEntity
from core.domain.repositories import IReadingRepository
from core.infra.orm.reading import Reading as ReadingModel

# Importando o Enum definido no domínio para uso na interface
from core.domain.entity.reading import ReadingStatus


class ReadingRepository(IReadingRepository):
    """
    Implementação do repositório para o domínio Reading usando SQLAlchemy.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    # --- Método Auxiliar de Conversão ---
    def _to_entity(self, model: ReadingModel) -> ReadingEntity:
        """Converte um modelo ORM em uma entidade de domínio."""
        # Nota: Assumindo que a entidade Reading tem campos para _current_chapter,
        # _progress, _status, etc., que podem ser inicializados diretamente.
        # Caso sua entidade use dataclass, ela receberia os campos com underscore.
        return ReadingEntity(
            id=model.id,
            id_user=model.id_user,
            id_manga=model.id_manga,
            start_date=model.start_date,
            _current_chapter=model.current_chapter,
            _progress=model.progress,
            _status=ReadingStatus(model.status),  # Converte str do DB para Enum
            _notes=model.notes,
        )

    # ----------------------------------------------------------------------
    # Implementação dos Métodos da Interface
    # ----------------------------------------------------------------------

    async def save(self, reading: ReadingEntity) -> None:
        """Cria um novo registro de leitura."""
        # Mapeia a entidade para o modelo ORM
        reading_model = ReadingModel(
            id=reading.id,
            id_user=reading.id_user,
            id_manga=reading.id_manga,
            start_date=reading.start_date,
            current_chapter=reading.current_chapter,  # usa o getter da entidade
            progress=reading.progress,
            status=reading.status.value,  # Pega o valor string do Enum
            notes=reading.notes,
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
            # 2. Atualizar os atributos mutáveis do modelo com os valores da entidade
            reading_model.current_chapter = reading.current_chapter
            reading_model.progress = reading.progress
            reading_model.status = reading.status.value
            reading_model.notes = reading.notes

            # 3. Commitar as mudanças
            await self.session.commit()
            return self._to_entity(reading_model)

        return reading

    async def delete(self, id_manga: str, id_user: str) -> None:
        """Deleta o registro de leitura específico."""

        # O SQLAlchemy permite a exclusão direta por filtro (mais eficiente)
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
        """Busca uma leitura específica por usuário e mangá."""

        result = await self.session.execute(
            sql_select(ReadingModel).where(
                ReadingModel.id_user == id_user, ReadingModel.id_manga == id_manga
            )
        )
        reading_model = result.scalar_one_or_none()

        if reading_model:
            return self._to_entity(reading_model)
        return None
