import dataclasses


@dataclasses.dataclass(frozen=True)
class Nickname:
    value: str

    def __post_init__(self):
        if not self.validate(self.value):
            raise ValueError("Invalid nickname")

    @staticmethod
    def validate(nickname: str) -> bool:
        return len(nickname) > 0
