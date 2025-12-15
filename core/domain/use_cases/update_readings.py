
# Importações corrigidas: Adicionando IMangaRepository
from core.domain.entity import Reading, ReadingStatus
from core.domain.repositories import IMangaRepository, IReadingRepository


class UpdateReading:
    """
    Use Case para atualizar o progresso de leitura de um registro existente.
    Agora busca o total_chapters do MangaRepository internamente.
    """

    def __init__(
        self,
        reading_repository: IReadingRepository,
        manga_repository: IMangaRepository,  # <-- NOVO: Injetando a dependência do Manga
    ):
        self.reading_repository = reading_repository
        self.manga_repository = manga_repository  # <-- NOVO: Armazenando o repositório

    async def execute(
        self,
        id_user: str,
        id_manga: str,
        new_current_chapter: int,
    ) -> Reading:
        """
        Busca o registro de leitura, obtém o total_chapters do mangá e atualiza
        o capítulo, progresso e status.
        """

        # 1. 🔍 BUSCAR O MANGÁ E VALIDAR TOTAL_CHAPTERS (Lógica movida para o corpo)
        manga = await self.manga_repository.find_by_id(id_manga)
        if not manga:
            raise ValueError("Manga not found")

        total_chapters = manga.total_chapters

        reading_to_update = await self.reading_repository.find_by_user_and_manga(
            id_user, id_manga
        )

        if not reading_to_update:
            raise ValueError("Read log not found.")

        # --- Lógica de Cálculo de Progresso e Status ---

        new_progress: float = 0.0

        if total_chapters > 0:
            raw_progress = new_current_chapter / total_chapters
            # Usando 1.0 para limitar o progresso a 100%
            new_progress = min(raw_progress, 1.0)

        # Define o status
        if new_current_chapter >= total_chapters and total_chapters > 0:
            new_status = ReadingStatus.COMPLETED
        # Mantive a lógica de status que você forneceu:
        elif new_current_chapter > 0:
            new_status = ReadingStatus.READING
        else:
            new_status = ReadingStatus.READING

        reading_to_update.update_progress(
            current_chapter=new_current_chapter,
            progress=new_progress,
            status=new_status,
        )

        await self.reading_repository.update(reading_to_update)

        return reading_to_update
