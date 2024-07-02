from src.practice_2.BankAccount import BankAccount
import pytest


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (342, 158),
                             (56.5, 443.5)
                         ])
def test_withdraw_positive(value, extend_result):
    acc = BankAccount()
    acc.deposit(500)

    assert acc.withdraw(value) is None
    assert acc.get_balance() == extend_result


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (-10, pytest.raises(ValueError)),
                             ("str", pytest.raises(TypeError)),
                             (1000, pytest.raises(ValueError))
                         ])
def test_withdraw_negative(value, extend_result):
    acc = BankAccount()
    acc.deposit(500)

    with extend_result:
        assert acc.withdraw(value)
        assert acc.get_balance() == extend_result
