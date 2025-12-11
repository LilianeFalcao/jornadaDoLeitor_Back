import pytest

from core.domain.value_objects import Name


def test_should_create_a_valid_name():
    name = Name("John Doe")
    assert name.value == "John Doe"


def test_should_raise_error_for_invalid_name():
    with pytest.raises(ValueError, match="Invalid name"):
        Name("")
