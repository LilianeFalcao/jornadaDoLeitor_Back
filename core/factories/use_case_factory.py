from typing import Optional

from core.domain.repositories import (
    IMangaRepository,
    IReadingRepository,
    IUserRepository,
)
from core.domain.use_cases import (
    DeleteUser,
    FindUser,
    FindUserByEmail,
    LoginUser,
    RegisterUser,
    UpdateUser,
)
from core.infra.mock import (
    MockMangaRepository,
    MockReadingRepository,
    MockUserRepository,
)


class UseCaseFactory:
    def __init__(
        self,
        manga_repository: Optional[IMangaRepository] = None,
        reading_repository: Optional[IReadingRepository] = None,
        user_repository: Optional[IUserRepository] = None,
    ):
        self.manga_repository = manga_repository or MockMangaRepository()
        self.reading_repository = reading_repository or MockReadingRepository()
        self.user_repository = user_repository or MockUserRepository()

    # ----------------------------------------------------------------------
    # Implementação Manga
    # ----------------------------------------------------------------------

    # ----------------------------------------------------------------------
    # Implementação Reading
    # ----------------------------------------------------------------------

    # ----------------------------------------------------------------------
    # Implementação User
    # ----------------------------------------------------------------------
    def create_register_user(self) -> RegisterUser:
        return RegisterUser(user_repository=self.user_repository)

    def create_login_user(self) -> LoginUser:
        return LoginUser(user_repository=self.user_repository)

    def create_find_user(self) -> FindUser:
        return FindUser(user_repository=self.user_repository)

    def create_find_user_by_email(self) -> FindUserByEmail:
        return FindUserByEmail(user_repository=self.user_repository)

    def create_update_user(self) -> UpdateUser:
        return UpdateUser(user_repository=self.user_repository)

    def create_delete_user(self) -> DeleteUser:
        return DeleteUser(user_repository=self.user_repository)
