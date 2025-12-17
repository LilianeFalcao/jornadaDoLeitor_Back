from typing import Optional
from core.domain.entity import Reading, ReadingStatus
from core.domain.repositories import IMangaRepository, IReadingRepository


class UpdateReading:
    def __init__(
        self,
        reading_repository: IReadingRepository,
        manga_repository: IMangaRepository,
    ):
        self.reading_repository = reading_repository
        self.manga_repository = manga_repository

    async def execute(
        self,
        id_user: str,
        id_manga: str,
        current_chapter: Optional[int] = None,
        notes: Optional[str] = None,
    ) -> Reading:
        reading = await self.reading_repository.find_by_user_and_manga(
            id_user, id_manga
        )
        if not reading:
            raise ValueError("Read log not found")

        if notes is not None:
            reading.update_notes(notes)

        if current_chapter is not None:
            manga = await self.manga_repository.find_by_id(id_manga)
            if not manga:
                raise ValueError("Manga not found")

            total_chapters = manga.total_chapters or 0

            progress = (
                min(current_chapter / total_chapters, 1.0)
                if total_chapters > 0
                else 0.0
            )

            status = (
                ReadingStatus.COMPLETED
                if total_chapters > 0 and current_chapter >= total_chapters
                else ReadingStatus.READING
            )

            reading.update_progress(
                current_chapter=current_chapter,
                progress=progress,
                status=status,
            )

        await self.reading_repository.update(reading)

        return reading
