from datetime import datetime

import pytest

from core.domain.entities import Loan


def test_should_create_a_valid_loan():
    loan = Loan(
        id="123", user_id="456", vinyl_record_id="789", loan_date=datetime(2025, 1, 1)
    )
    assert loan.id == "123"
    assert loan.user_id == "456"
    assert loan.vinyl_record_id == "789"
    assert loan.loan_date == datetime(2025, 1, 1)
    assert loan.return_date is None


def test_should_return_a_loan():
    loan = Loan(
        id="123", user_id="456", vinyl_record_id="789", loan_date=datetime(2025, 1, 1)
    )
    returned_loan = loan.return_loan()
    assert returned_loan.return_date is not None


def test_should_raise_error_when_returning_an_already_returned_loan():
    loan = Loan(
        id="123",
        user_id="456",
        vinyl_record_id="789",
        loan_date=datetime(2025, 1, 1),
        return_date=datetime(2025, 1, 10),
    )
    with pytest.raises(ValueError, match="Loan already returned"):
        loan.return_loan()
