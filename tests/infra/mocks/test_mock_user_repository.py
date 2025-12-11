import pytest

from core.domain.entities import User
from core.domain.value_objects import Email, Name, Password
from core.infra.mocks import MockUserRepository


def create_user(
    id: str = None,
    name: str = "Test User",
    email: str = "test@example.com",
    password: str = "ValidPass1!",
) -> User:
    import uuid

    return User(
        id=id or str(uuid.uuid4()),
        name=Name(name),
        email=Email(email),
        password=Password(password),
    )


@pytest.mark.asyncio
async def test_save_and_find_by_id():
    repo = MockUserRepository()
    user = create_user()
    await repo.save(user)

    assert len(repo.users) == 1
    found_user = await repo.find_by_id(user.id)
    assert found_user == user

    not_found_user = await repo.find_by_id("non-existent-id")
    assert not_found_user is None


@pytest.mark.asyncio
async def test_find_by_email():
    repo = MockUserRepository()
    user = create_user(email="specific@email.com")
    await repo.save(user)

    found_user = await repo.find_by_email("specific@email.com")
    assert found_user == user

    not_found_user = await repo.find_by_email("non-existent@email.com")
    assert not_found_user is None


@pytest.mark.asyncio
async def test_update_user():
    repo = MockUserRepository()
    user = create_user()
    await repo.save(user)

    updated_user = User(
        id=user.id, name=Name("Updated Name"), email=user.email, password=user.password
    )
    await repo.update(updated_user)

    found_user = await repo.find_by_id(user.id)
    assert found_user.name.value == "Updated Name"
    assert len(repo.users) == 1


@pytest.mark.asyncio
async def test_delete_user():
    repo = MockUserRepository()
    user1 = create_user()
    user2 = create_user()
    await repo.save(user1)
    await repo.save(user2)

    await repo.delete(user1.id)

    assert len(repo.users) == 1
    assert await repo.find_by_id(user1.id) is None
    assert await repo.find_by_id(user2.id) is not None
