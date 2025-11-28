import dataclasses
import re


@dataclasses.dataclass(frozen=True)
class Password:
    value: str

    def __post_init__(self):
        self.validate(self.value)

    @staticmethod
    def validate(password: str) -> bool:
        if len(password) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres")
        if not re.search(r"[A-Z]", password):
            raise ValueError("A senha deve ter pelo menos uma letra maiúscula")
        if not re.search(r"[a-z]", password):
            raise ValueError("A senha deve ter pelo menos uma letra minúscula")
        if not re.search(r"[0-9]", password):
            raise ValueError("A senha deve ter pelo menos um número")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("A senha deve conter pelo menos um caractere especial")
        return True
