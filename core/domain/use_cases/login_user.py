from ..entities import User
from ..repositories import IUserRepository


class LoginUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> User:
        user = await self.user_repository.find_by_email(email)

        if not user:
            raise ValueError("Invalid credentials")

        if not self._compare_password(password, user.password.value):
            raise ValueError("Invalid credentials")

        return user

    def _compare_password(self, password: str, hashed_password: str) -> bool:
        return f"hashed_{password}" == hashed_password
