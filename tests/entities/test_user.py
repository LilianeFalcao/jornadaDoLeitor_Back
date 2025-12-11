from core.domain.entities import User
from core.domain.value_objects import Email, Name, Password


def test_should_create_a_valid_user():
    user = User(
        id="123",
        name=Name("Test User"),
        email=Email("test@example.com"),
        password=Password("ValidPass1!"),
    )
    assert user.id == "123"
    assert user.name.value == "Test User"
    assert user.email.value == "test@example.com"
    assert user.password.value == "ValidPass1!"
