from typing import List, Optional

from core.domain.entity import User
from core.domain.repositories import IUserRepository

from sqlalchemy.ext.asyncio import AsyncSession
from core.infra.orm.user import User as UserModel

from sqlalchemy.future import select

from core.domain.value_objects import Email, Nickname, Password
from core.security import get_password_hash


class MockUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        hashed_pass = get_password_hash(user.password.value)
        user_model = UserModel(
            id=user.id,
            nickname=user.nickname.value,
            email=user.email.value,
            password=hashed_pass,
        )
        self.session.add(user_model)
        await self.session.commit()
        # self.users.append(user)

    async def find_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email.value == email), None)

        # return next((user for user in self.users if user.email.value == email), None)

    async def find_by_id(self, id: str) -> Optional[User]:
        return next((user for user in self.users if user.id == id), None)

    async def update(self, user: User) -> None:
        index = next((i for i, u in enumerate(self.users) if u.id == user.id), None)
        if index is not None:
            self.users[index] = user

    async def delete(self, id: str) -> None:
        self.users = [user for user in self.users if user.id != id]
