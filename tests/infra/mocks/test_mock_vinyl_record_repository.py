import pytest

from core.domain.entities import VinylRecord
from core.domain.value_objects import Name, Photo
from core.infra.mocks import MockVinylRecordRepository


def create_vinyl_record(
    id: str = None,
    band: str = "Test Band",
    album: str = "Test Album",
    year: int = 2025,
    number_of_tracks: int = 10,
    photo_url: str = "http://example.com/photo.jpg",
    user_id: str = None,
) -> VinylRecord:
    import uuid

    return VinylRecord(
        id=id or str(uuid.uuid4()),
        band=Name(band),
        album=Name(album),
        year=year,
        number_of_tracks=number_of_tracks,
        photo=Photo(photo_url),
        user_id=user_id or str(uuid.uuid4()),
    )


@pytest.mark.asyncio
async def test_save_and_find_by_id():
    repo = MockVinylRecordRepository()
    record = create_vinyl_record()
    await repo.save(record)

    assert len(repo.records) == 1
    found_record = await repo.find_by_id(record.id)
    assert found_record == record

    not_found_record = await repo.find_by_id("non-existent-id")
    assert not_found_record is None


@pytest.mark.asyncio
async def test_find_all():
    repo = MockVinylRecordRepository()
    record1 = create_vinyl_record()
    record2 = create_vinyl_record()
    await repo.save(record1)
    await repo.save(record2)

    all_records = await repo.find_all()
    assert len(all_records) == 2
    assert record1 in all_records
    assert record2 in all_records


@pytest.mark.asyncio
async def test_update():
    repo = MockVinylRecordRepository()
    record = create_vinyl_record()
    await repo.save(record)

    updated_record = VinylRecord(
        id=record.id,
        band=Name("Updated Band"),
        album=record.album,
        year=record.year,
        number_of_tracks=record.number_of_tracks,
        photo=record.photo,
        user_id=record.user_id,
    )
    await repo.update(updated_record)

    found_record = await repo.find_by_id(record.id)
    assert found_record.band.value == "Updated Band"
    assert len(repo.records) == 1


@pytest.mark.asyncio
async def test_delete():
    repo = MockVinylRecordRepository()
    record1 = create_vinyl_record()
    record2 = create_vinyl_record()
    await repo.save(record1)
    await repo.save(record2)

    await repo.delete(record1.id)

    assert len(repo.records) == 1
    assert await repo.find_by_id(record1.id) is None
    assert await repo.find_by_id(record2.id) is not None
