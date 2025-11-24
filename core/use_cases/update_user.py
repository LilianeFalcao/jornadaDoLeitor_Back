from typing import Optional

from ..entities import User
from ..repositories import IUserRepository
from ..value_objects import Email, Name


class UpdateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(
        self, id: str, name: Optional[str] = None, email: Optional[str] = None
    ) -> User:
        user = await self.user_repository.find_by_id(id)

        if not user:
            raise ValueError("User not found")

        new_name = Name(name) if name else user.name
        new_email = Email(email) if email else user.email

        updated_user = User(
            id=user.id,
            name=new_name,
            email=new_email,
            password=user.password,
        )

        await self.user_repository.update(updated_user)
        return updated_user
