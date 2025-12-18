import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.infra.orm.manga import Manga as MangaModel


@pytest.mark.asyncio
async def test_create_reading(client: AsyncClient, auth_headers, session: AsyncSession):
    manga_id = "90a5f852-4101-41a7-8c92-fa12437424ae"

    new_manga = MangaModel(id=manga_id, title="Fullmetal Alchemist", total_chapters=108)
    session.add(new_manga)
    await session.commit()
    response = await client.post(
        "/api/readings",
        headers=auth_headers,
        json={
            "id_manga": manga_id,
            "start_date": "2025-12-18T00:20:53.634Z",
            "current_chapter": 26,
            "notes": "muito divertido",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["current_chapter"] == 26
    assert data["notes"] == "muito divertido"
    assert "id" in data
