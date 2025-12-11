import pytest

from core.domain.value_objects import Password


def test_should_create_a_valid_password():
    password = Password("ValidPass1!")
    assert password.value == "ValidPass1!"


def test_should_raise_error_for_short_password():
    with pytest.raises(ValueError, match="A senha deve ter pelo menos 8 caracteres"):
        Password("short")


def test_should_raise_error_for_password_without_uppercase():
    with pytest.raises(
        ValueError, match="A senha deve ter pelo menos uma letra maiúscula"
    ):
        Password("nouppercase1!")


def test_should_raise_error_for_password_without_lowercase():
    with pytest.raises(
        ValueError, match="A senha deve ter pelo menos uma letra minúscula"
    ):
        Password("NOLOWERCASE1!")


def test_should_raise_error_for_password_without_number():
    with pytest.raises(ValueError, match="A senha deve ter pelo menos um número"):
        Password("NoNumber!")


def test_should_raise_error_for_password_without_special_char():
    with pytest.raises(
        ValueError, match="A senha deve conter pelo menos um caractere especial"
    ):
        Password("NoSpecialChar1")
