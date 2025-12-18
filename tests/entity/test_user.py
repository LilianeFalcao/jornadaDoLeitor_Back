from core.domain.entity import User

from core.domain.value_objects import Email, Nickname, Password


def test_should_create_a_valid_user():
    user = User(
        id="123",
        nickname=Nickname("Test User"),
        email=Email("test@example.com"),
        password=Password("ValidPass1!"),
    )
    assert user.id == "123"
    assert user.nickname.value == "Test User"
    assert user.email.value == "test@example.com"
    assert user.password.value == "ValidPass1!"
