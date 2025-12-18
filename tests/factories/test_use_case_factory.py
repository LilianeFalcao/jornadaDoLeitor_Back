from core.infra.mock import (
    MockMangaRepository,
    MockUserRepository,
    MockReadingRepository,
)

from core.domain.use_cases import RegisterUser
from core.factories.use_case_factory import UseCaseFactory


def test_should_create_use_case_with_internal_mocks():
    factory = UseCaseFactory()
    register_user_use_case = factory.create_register_user()

    assert isinstance(register_user_use_case, RegisterUser)
    assert isinstance(register_user_use_case.user_repository, MockUserRepository)


def test_should_create_use_case_with_external_mocks():
    user_repo = MockUserRepository()

    factory = UseCaseFactory(
        user_repository=user_repo,
    )

    borrow_use_case = factory.create_borrow_vinyl_record()
    assert borrow_use_case.user_repository is user_repo
