# core/domain/use_cases/__init__.py

# Use Cases de Usuário
from .register_user import RegisterUser
from .find_user import FindUser
from .login_user import LoginUser
from .find_user_by_email import FindUserByEmail
from .delete_user import DeleteUser
from .update_user import UpdateUser

# Use Cases de Leitura
from .add_reading import AddReading
from .list_reading_by_user import ListUserReading

# Use Cases de Mangá
from .find_all_mangas import FindAllMangas

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
]
