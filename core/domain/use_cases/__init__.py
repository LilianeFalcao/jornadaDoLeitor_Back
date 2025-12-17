# core/domain/use_cases/__init__.py

# Use Cases de Usuário
from .find_user import FindUser
from .find_user_by_email import FindUserByEmail
from .list_reading_by_user import ListUserReading
from .login_user import LoginUser
from .register_user import RegisterUser
from .update_user import UpdateUser
from .delete_user import DeleteUser

# Use Cases de Leitura
from .add_reading import AddReading
from .update_readings import UpdateReading
from .delete_reading import DeleteReading
from .find_reading_by_id_and_user import FindReadingByIdAndUser
from .find_by_user_and_manga import FindReadingByUserAndManga

# from .find_by_user_and_manga import FindReadingByUserAndManga
# Use Cases de Mangá
from .find_all_mangas import FindAllMangas
from .add_manga import AddManga


# Opcional, mas recomendado: Define o que será exportado quando
# alguém fizer 'from core.domain.use_cases import *'
__all__ = [
    "RegisterUser",
    "FindUser",
    "LoginUser",
    "FindUserByEmail",
    "DeleteUser",
    "UpdateUser",
    "DeleteReading",
    "UpdateReading",
    "FindReadingByUserAndManga",
    "FindReadingByIdAndUser",
    "AddReading",
    "ListUserReading",
    "FindAllMangas",
    "AddManga",
]
