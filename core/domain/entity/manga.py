import dataclasses


@dataclasses.dataclass(frozen=True)
class Manga:
    id: str
    img_url: str
    title: str
    author_name: str
    gender: str
    total_chapters: int
