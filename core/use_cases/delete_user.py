from ..repositories import IUserRepository


class DeleteUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, id: str) -> None:
        user = await self.user_repository.find_by_id(id)

        if not user:
            raise ValueError("User not found")

        await self.user_repository.delete(id)
