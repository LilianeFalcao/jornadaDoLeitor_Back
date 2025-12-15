import dataclasses


@dataclasses.dataclass(frozen=True)
class Manga:
    id: str
    img_URL: str
    title: str
    author_name: str
    gender: str
    total_chapters: int
