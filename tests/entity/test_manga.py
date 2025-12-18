from core.domain.entity import Manga


def test_should_create_a_manga():
    manga = Manga(
        id="123",
        img_URL="https://exaple.com/imagejpg",
        title="Fullmetal Alchemist",
        author_name="Hiromu Arakawa",
        gender="Shounen",
        total_chapters=118,
    )
    assert manga.id == "123"
    assert manga.img_URL == "https://exaple.com/imagejpg"
    assert manga.title == "Fullmetal Alchemist"
    assert manga.author_name == "Hiromu Arakawa"
    assert manga.gender == "Shounen"
    assert manga.total_chapters == 118
