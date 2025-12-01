import uuid

from ..entity import User
from ..repositories import IUserRepository
from ..value_objects import Email, Nickname, Password

from core.security import get_password_hash


class RegisterUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, nickname: str, email: str, password: str) -> User:
        user_exists = await self.user_repository.find_by_email(email)
        if user_exists:
            raise ValueError("User already exists")

        hashed_password = get_password_hash(password)

        user = User(
            id=str(uuid.uuid4()),
            nickname=Nickname(nickname),
            email=Email(email),
            password=Password(hashed_password),
        )

        await self.user_repository.save(user)
        return user
