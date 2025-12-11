from datetime import datetime

import pytest

from core.domain.entities import Loan
from core.infra.mocks import MockLoanRepository


def create_loan(
    id: str = None,
    user_id: str = None,
    vinyl_record_id: str = None,
    loan_date: datetime = None,
    return_date: datetime = None,
) -> Loan:
    import uuid

    return Loan(
        id=id or str(uuid.uuid4()),
        user_id=user_id or str(uuid.uuid4()),
        vinyl_record_id=vinyl_record_id or str(uuid.uuid4()),
        loan_date=loan_date or datetime.now(),
        return_date=return_date,
    )


@pytest.mark.asyncio
async def test_save_and_find_by_id():
    repo = MockLoanRepository()
    loan = create_loan()
    await repo.save(loan)

    assert len(repo.loans) == 1
    found_loan = await repo.find_by_id(loan.id)
    assert found_loan == loan

    not_found_loan = await repo.find_by_id("non-existent-id")
    assert not_found_loan is None


@pytest.mark.asyncio
async def test_find_by_user_id():
    repo = MockLoanRepository()
    loan1 = create_loan(user_id="user1")
    loan2 = create_loan(user_id="user1")
    loan3 = create_loan(user_id="user2")
    await repo.save(loan1)
    await repo.save(loan2)
    await repo.save(loan3)

    user1_loans = await repo.find_by_user_id("user1")
    assert len(user1_loans) == 2
    assert loan1 in user1_loans
    assert loan2 in user1_loans


@pytest.mark.asyncio
async def test_find_current_loan_of_record():
    repo = MockLoanRepository()
    active_loan = create_loan(vinyl_record_id="record1", return_date=None)
    returned_loan = create_loan(vinyl_record_id="record1", return_date=datetime.now())
    other_loan = create_loan(vinyl_record_id="record2", return_date=None)

    await repo.save(active_loan)
    await repo.save(returned_loan)
    await repo.save(other_loan)

    current_loan = await repo.find_current_loan_of_record("record1")
    assert current_loan == active_loan

    no_loan = await repo.find_current_loan_of_record("non-existent-record")
    assert no_loan is None


@pytest.mark.asyncio
async def test_update():
    repo = MockLoanRepository()
    loan = create_loan()
    await repo.save(loan)

    updated_loan = loan.return_loan()

    await repo.update(updated_loan)

    found_loan = await repo.find_by_id(loan.id)
    assert found_loan.return_date is not None
    assert len(repo.loans) == 1
