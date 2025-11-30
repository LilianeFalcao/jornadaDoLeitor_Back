from typing import List, Optional

from core.domain.entity import User
from core.domain.repositories import IUserRepository


class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users: List[User] = []

    async def save(self, user: User) -> None:
        self.users.append(user)

    async def find_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email.value == email), None)

    async def find_by_id(self, id: str) -> Optional[User]:
        return next((user for user in self.users if user.id == id), None)

    async def update(self, user: User) -> None:
        index = next((i for i, u in enumerate(self.users) if u.id == user.id), None)
        if index is not None:
            self.users[index] = user

    async def delete(self, id: str) -> None:
        self.users = [user for user in self.users if user.id != id]
