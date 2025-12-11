import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post(
        "/api/users",
        json={
            "nickname": "New User",
            "email": "new@example.com",
            "password": "Password123!",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nickname"] == "New User"
    assert data["email"] == "new@example.com"
    assert "id" in data

