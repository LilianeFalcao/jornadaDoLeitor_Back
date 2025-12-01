from ..entity import User
from ..repositories import IUserRepository

from core.security import verify_password


class LoginUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> User:
        user = await self.user_repository.find_by_email(email)

        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password.value):
            raise ValueError("Invalid credentials")

        return user
