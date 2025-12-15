import uuid
from datetime import datetime
from typing import Optional

# Importações assumidas com base na sua estrutura de projeto
from core.domain.entity import Reading, ReadingStatus
from core.domain.repositories import (
    IMangaRepository,
    IReadingRepository,
    IUserRepository,
)

# Nota: Assumindo que ReadingStatus é importado do domínio (core.domain.entities ou core.domain.enums)


class AddReading:
    """
    Use Case para adicionar ou atualizar o progresso de leitura de um mangá.
    """

    def __init__(
        self,
        reading_repository: IReadingRepository,
        user_repository: IUserRepository,
        manga_repository: IMangaRepository,
    ):
        self.reading_repository = reading_repository
        self.user_repository = user_repository
        self.manga_repository = manga_repository

    async def execute(
        self,
        id_user: str,
        id_manga: str,
        current_chapter: int,
        notes: Optional[str] = None,
    ) -> Reading:
        """
        Executa a lógica de adicionar/atualizar a leitura.
        """

        # 1. Validação de Dependências (User e Manga)

        # O método findById pode precisar ser renomeado para find_by_id em Python,
        # dependendo da sua interface. Assumimos find_by_id.
        user = await self.user_repository.find_by_id(id_user)
        if not user:
            raise ValueError("User not found")

        manga = await self.manga_repository.find_by_id(id_manga)
        if not manga:
            raise ValueError("Manga not found")

        # 2. Busca por Leitura Existente

        existing_reading = await self.reading_repository.find_by_user_and_manga(
            id_user, id_manga
        )

        # 3. Cálculo de Status e Progresso

        # Garante que não haja divisão por zero ou que total_chapters seja válido
        if manga.total_chapters <= 0:
            # Tratar mangás sem capítulos totais definidos
            progress = 0.0
        else:
            # O progresso é tipicamente um float (0.0 a 1.0)
            progress = min(current_chapter / manga.total_chapters, 1.0)

        status: ReadingStatus = (
            ReadingStatus.COMPLETED
            if current_chapter >= manga.total_chapters
            else ReadingStatus.READING
        )

        # 4. Lógica de Atualização (se a leitura existir)

        if existing_reading:
            # Chama o método de atualização da entidade (mutabilidade controlada)
            existing_reading.update_progress(
                current_chapter=current_chapter, progress=progress, status=status
            )

            if notes is not None:
                existing_reading.update_notes(notes)

            # Persiste a entidade atualizada
            return await self.reading_repository.update(existing_reading)

        # 5. Lógica de Criação (se a leitura não existir)

        # Cria a nova entidade usando o Factory Method ou Construtor,
        # dependendo da sua definição de entidade Reading.
        # Estamos usando o padrão de dataclass/construtor do seu exemplo RegisterVinylRecord:

        new_reading = Reading(
            id=str(
                uuid.uuid4()
            ),  # Geração de ID único (similar a Math.random().toString())
            id_user=id_user,
            id_manga=id_manga,
            start_date=datetime.now(),  # Data de início é a data de criação
            _current_chapter=current_chapter,
            _progress=progress,
            _status=status,
            _notes=notes if notes is not None else "",
        )

        await self.reading_repository.save(new_reading)

        return new_reading
