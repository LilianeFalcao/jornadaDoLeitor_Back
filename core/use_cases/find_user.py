from typing import Optional

from ..entities import User
from ..repositories import IUserRepository


class FindUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, id: str) -> Optional[User]:
        return await self.user_repository.find_by_id(id)
