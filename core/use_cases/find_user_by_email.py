from typing import Optional

from ..entities import User
from ..repositories import IUserRepository


class FindUserByEmail:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str) -> Optional[User]:
        return await self.user_repository.find_by_email(email)
