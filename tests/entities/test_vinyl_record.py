from core.domain.entities import VinylRecord
from core.domain.value_objects import Name, Photo


def test_should_create_a_valid_vinyl_record():
    record = VinylRecord(
        id="123",
        band=Name("Test Band"),
        album=Name("Test Album"),
        year=2025,
        number_of_tracks=10,
        photo=Photo("http://example.com/photo.jpg"),
        user_id="456",
    )
    assert record.id == "123"
    assert record.band.value == "Test Band"
    assert record.album.value == "Test Album"
    assert record.year == 2025
    assert record.number_of_tracks == 10
    assert record.photo.url == "http://example.com/photo.jpg"
    assert record.user_id == "456"
