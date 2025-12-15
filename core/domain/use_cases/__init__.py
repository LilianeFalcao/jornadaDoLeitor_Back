# core/domain/use_cases/__init__.py

# Use Cases de Usuário
from .find_user import FindUser
from .find_user_by_email import FindUserByEmail
from .list_reading_by_user import ListUserReading
from .login_user import LoginUser
from .register_user import RegisterUser
from .update_user import UpdateUser

# Use Cases de Leitura
from .add_reading import AddReading
from .update_readings import UpdateReading
from .delete_user import DeleteUser

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
    "AddReading",
    "ListUserReading",
    "FindAllMangas",
    "AddManga",
]
