import dataclasses
import re


@dataclasses.dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not self.validate(self.value):
            raise ValueError("E-mail inválido")

    @staticmethod
    def validate(email: str) -> bool:
        email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        return bool(email_regex.match(email))
