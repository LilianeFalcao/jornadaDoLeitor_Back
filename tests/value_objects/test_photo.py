import pytest

from core.domain.value_objects import Photo


def test_should_create_a_valid_photo():
    photo = Photo("http://example.com/photo.jpg")
    assert photo.url == "http://example.com/photo.jpg"


def test_should_raise_error_for_invalid_photo_url():
    with pytest.raises(ValueError, match="Invalid photo URL"):
        Photo("invalid-url")


def test_should_raise_error_for_empty_photo_url():
    with pytest.raises(ValueError, match="Invalid photo URL"):
        Photo("")
