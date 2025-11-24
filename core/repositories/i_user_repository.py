from abc import ABC, abstractmethod
from typing import Optional

from ..entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def find_by_id(self, id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def update(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
