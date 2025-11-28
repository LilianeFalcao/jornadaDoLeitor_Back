import uuid

from ..entities import User
from ..repositories import IUserRepository
from ..value_objects import Email, Name, Password


class RegisterUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, name: str, email: str, password: str) -> User:
        user_exists = await self.user_repository.find_by_email(email)
        if user_exists:
            raise ValueError("User already exists")

        hashed_password = self._hash_password(password)

        user = User(
            id=str(uuid.uuid4()),
            name=Name(name),
            email=Email(email),
            password=Password(hashed_password),
        )

        await self.user_repository.save(user)
        return user

    def _hash_password(self, password: str) -> str:
        return f"hashed_{password}"
