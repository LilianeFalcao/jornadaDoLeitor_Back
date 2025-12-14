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
    AddReading,  # Use Case precisa de 3 repositórios
    AddManga,
    UpdateUser,
    ListUserReading,  # Use Case precisa de 1 repositório
    FindAllMangas,
)
from core.infra.mock import (
    MockMangaRepository,
    MockReadingRepository,
    MockUserRepository,
)


class UseCaseFactory:
    """
    Fábrica responsável por instanciar todos os Use Cases, injetando
    as dependências (repositórios) corretas.
    """

    def __init__(
        self,
        manga_repository: Optional[IMangaRepository] = None,
        reading_repository: Optional[IReadingRepository] = None,
        user_repository: Optional[IUserRepository] = None,
    ):
        # Define os repositórios reais ou Mocks se não forem fornecidos
        self.manga_repository = manga_repository or MockMangaRepository()
        self.reading_repository = reading_repository or MockReadingRepository()
        self.user_repository = user_repository or MockUserRepository()

    # ----------------------------------------------------------------------
    # Implementação Manga
    # ----------------------------------------------------------------------
    def create_find_mangas_all(self) -> FindAllMangas:
        return FindAllMangas(mangas_repository=self.manga_repository)

    def create_add_mangas(self) -> AddManga:
        return AddManga(mangas_repository=self.manga_repository)
    # ----------------------------------------------------------------------
    # Implementação Reading (CORRIGIDO)
    # ----------------------------------------------------------------------
    def create_add_reading(self) -> AddReading:
        """
        Cria o Use Case AddReading, injetando todos os 3 repositórios
        necessários (Reading, User, Manga).
        """
        return AddReading(
            reading_repository=self.reading_repository,
            user_repository=self.user_repository,
            manga_repository=self.manga_repository,
        )

    def create_list_reading_by_user(self) -> ListUserReading:
        """
        Cria o Use Case ListUserReading, injetando apenas o ReadingRepository.
        """
        # Nota: O nome do parâmetro deve coincidir com o __init__ do ListUserReading
        return ListUserReading(reading_repository=self.reading_repository)

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
