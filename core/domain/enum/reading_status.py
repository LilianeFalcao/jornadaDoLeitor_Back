import enum


class ReadingStatus(str, enum.Enum):
    READING = "reading"
    COMPLETED = "completed"

    @classmethod
    def _missing_(cls, value):
        """
        Este método é chamado quando o SQLAlchemy tenta converter 'reading'
        e não encontra no Enum.
        """
        if isinstance(value, str):
            value_upper = value.upper()
            for member in cls:
                if member.value == value_upper:
                    return member
        return super()._missing_(value)
