import pytest

from core.domain.value_objects import Email


def test_should_create_a_valid_email():
    email = Email("test@example.com")
    assert email.value == "test@example.com"


def test_should_raise_error_for_invalid_email():
    with pytest.raises(ValueError, match="E-mail inválido"):
        Email("invalid-email")


def test_should_raise_error_for_empty_email():
    with pytest.raises(ValueError, match="E-mail inválido"):
        Email("")
