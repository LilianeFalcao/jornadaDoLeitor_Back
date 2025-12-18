import pytest

from core.domain.entity import Manga
from core.infra.mock.mock_manga_repository import MockMangaRepository


def create_mangas(
    id: str = None,
    img_URL: str = "http://example.com/cover.jpg",
    title: str = "Manga Test",
    author_name: str = "Author Test",
    gender: str = "Shonen",
    total_chapters: int = 100,
) -> Manga:
    import uuid

    return Manga(
        id=id or str(uuid.uuid4()),
        img_URL=img_URL,
        title=title,
        author_name=author_name,
        gender=gender,
        total_chapters=total_chapters,
    )


@pytest.mark.asyncio
async def test_save():
    repo = MockMangaRepository()
    manga = create_mangas()
    await repo.save(manga)

    assert len(repo.mangas) == 1
    found_manga = await repo.find_by_id(manga.id)
    assert found_manga == manga

    not_found_manga = await repo.find_by_id("non-existent-id")
    assert not_found_manga is None


@pytest.mark.asyncio
async def test_find_by_title():
    repo = MockMangaRepository()
    manga_1 = create_mangas(title="Fullmetal Alchemist")
    manga_2 = create_mangas(title="Naruto")

    await repo.save(manga_1)
    await repo.save(manga_2)

    found = await repo.find_by_title("Fullmetal Alchemist")

    assert found is not None
    assert found.title == "Fullmetal Alchemist"
    assert found.id == manga_1.id


@pytest.mark.asyncio
async def test_find_by_author_name():
    repo = MockMangaRepository()
    manga = create_mangas(author_name="Hiromu Arakawa")
    await repo.save(manga)

    results = await repo.find_by_author_name("Hiromu Arakawa")

    assert len(results) == 1
    assert results[0].author_name == "Hiromu Arakawa"
