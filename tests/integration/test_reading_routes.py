import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from core.infra.orm.manga import Manga as MangaModel


@pytest.mark.asyncio
async def test_create_reading(
    client: AsyncClient, auth_headers, db_session: AsyncSession
):
    manga_id = "eee6cbfe-bf0c-454c-8a96-ace546871ad9"

    new_manga = MangaModel(id=manga_id, title="Fullmetal Alchemist", total_chapters=108)
    db_session.add(new_manga)
    await db_session.commit()

    response = await client.post(
        "/api/readings",
        headers=auth_headers,
        json={
            "id_manga": manga_id,
            "start_date": "2025-12-18T00:20:53.634Z",
            "current_chapter": 55,
            "notes": "muito divertido",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["_current_chapter"] == 55
    assert data["_notes"] == "muito divertido"
    assert "id" in data


@pytest.mark.asyncio
async def test_update_reading(
    client: AsyncClient, auth_headers, db_session: AsyncSession
):
    manga_id = "eee6cbfe-bf0c-454c-8a96-ace546871ad9"

    new_manga = MangaModel(id=manga_id, title="Fullmetal Alchemist", total_chapters=108)
    db_session.add(new_manga)
    await db_session.commit()

    create = await client.post(
        "/api/readings",
        headers=auth_headers,
        json={
            "id_manga": manga_id,
            "start_date": "2025-12-18T00:20:53.634Z",
            "current_chapter": 55,
            "notes": "muito divertido",
        },
    )
    id_readings = create.json()["id_manga"]

    response = await client.put(
        f"/api/readings/{id_readings}",
        headers=auth_headers,
        json={
            "id_manga": id_readings,
            "start_date": "2025-12-18T00:20:53.634Z",
            "current_chapter": 60,
            "notes": "capitulo 60 me fez chorar",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["current_chapter"] == 60
    assert data["notes"] == "capitulo 60 me fez chorar"


@pytest.mark.asyncio
async def test_delete_readings(
    client: AsyncClient, auth_headers, db_session: AsyncSession
):
    manga_id = "eee6cbfe-bf0c-454c-8a96-ace546871ad9"

    new_manga = MangaModel(id=manga_id, title="Fullmetal Alchemist", total_chapters=108)
    db_session.add(new_manga)
    await db_session.commit()

    create = await client.post(
        "/api/readings",
        headers=auth_headers,
        json={
            "id_manga": manga_id,
            "start_date": "2025-12-18T00:20:53.634Z",
            "current_chapter": 55,
            "notes": "muito divertido",
        },
    )
    id_readings = create.json()["id"]

    response = await client.delete(f"/api/readings/{id_readings}", headers=auth_headers)
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_erro_reading(client: AsyncClient, auth_headers):
    response = await client.delete("/api/readings/1", headers=auth_headers)
    assert response.status_code == 404
