import dataclasses

from ..value_objects import Email, Nickname, Password


@dataclasses.dataclass
class User:
    id: str
    nickname: Nickname
    email: Email
    password: Password
