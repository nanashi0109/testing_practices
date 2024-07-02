from src.practice_2.BankAccount import BankAccount
import pytest


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (500, 500),
                         ])
def test_get_balance(value, extend_result):
    acc = BankAccount()
    acc.deposit(value)

    assert acc.get_balance() == extend_result
