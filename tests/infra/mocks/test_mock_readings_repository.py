import pytest
from datetime import datetime
from typing import Optional
import uuid

from core.domain.entity import Reading
from core.domain.enum.reading_status import (
    ReadingStatus,
)

from core.infra.mock import MockReadingRepository
from core.domain.enum.reading_status import ReadingStatus


def create_reading(
    id: str = None,
    start_date: datetime = None,
    current_chapter: int = 1,
    progress: float = 0.0,
    status: ReadingStatus = ReadingStatus.READING,
    notes: str = "",
    id_user: Optional[str] = None,
    id_manga: Optional[str] = None,
) -> Reading:
    return Reading(
        id=id or str(uuid.uuid4()),
        start_date=start_date or datetime.now(),
        _current_chapter=current_chapter,
        _progress=progress,
        _status=status,
        _notes=notes,
        id_user=id_user or str(uuid.uuid4()),
        id_manga=id_manga or str(uuid.uuid4()),
    )


# --------------------------------------
# Testa o save
# ---------------------------------------


@pytest.mark.asyncio
async def test_save_reading_find_by_user_id():
    repo = MockReadingRepository()
    readings = create_reading(id_user="user-123")
    await repo.save(readings)

    assert len(repo.readings) == 1
    found_reading = await repo.find_by_id_and_user(readings.id, "user-123")
    assert found_reading == readings
    not_found_reading = await repo.find_by_user_id("non-existent-id")
    assert not not_found_reading


# --------------------------------------
# Testa o Buscar todas as leituras por status.
# ---------------------------------------


@pytest.mark.asyncio
async def test_find_by_status():
    repo = MockReadingRepository()
    reading_1 = create_reading(id_user="user-123", status=ReadingStatus.COMPLETED)
    reading_2 = create_reading(id_user="user-456", status=ReadingStatus.COMPLETED)
    await repo.save(reading_1)
    await repo.save(reading_2)

    readings_status = await repo.find_by_status(ReadingStatus.COMPLETED)
    assert len(readings_status) == 2
    reading_1 in readings_status
    reading_2 in readings_status


# --------------------------------------
# Testa o update Leitura.
# ---------------------------------------


@pytest.mark.asyncio
async def test_update():
    repo = MockReadingRepository()
    readings = create_reading(id_user="user-123", current_chapter=1)
    await repo.save(readings)

    update_readings = Reading(
        id=readings.id,
        id_manga=readings.id_manga,
        id_user=readings.id_user,
        _current_chapter=65,
        _notes="capitulo 60 me fez chorar",
        _status=readings.status,
        _progress=readings.progress,
        start_date=readings.start_date,
    )
    await repo.update(update_readings)
    assert len(repo.readings) == 1
    found_reading = await repo.find_by_id_and_user(readings.id, "user-123")
    assert found_reading._current_chapter == 65
    assert found_reading._notes == "capitulo 60 me fez chorar"


@pytest.mark.asyncio
async def test_delete_reading():
    repo = MockReadingRepository()
    reading = create_reading(id_user="user-123", id_manga="manga-456")
    await repo.save(reading)

    assert len(repo.readings) == 1
    await repo.delete(id_manga="manga-456", id_user="user-123")
    assert len(repo.readings) == 0
    found = await repo.find_by_user_and_manga("user-123", "manga-456")
    assert found is None
