import pytest

from core.domain.value_objects import Nickname


def test_should_create_a_valid_nickname():
    nickname = Nickname("Hawks")
    assert nickname.value == "Hawks"


def test_should_raise_error_for_invalid_nickname():
    with pytest.raises(ValueError, match="Invalid nickname"):
        Nickname("")
