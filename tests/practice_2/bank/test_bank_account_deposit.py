from src.practice_2.BankAccount import BankAccount
import pytest


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (50, 50),
                             (25.2, 25.2)
                         ])
def test_deposit_positive(value, extend_result):
    acc = BankAccount()

    assert acc.deposit(value) is None
    assert acc.get_balance() == extend_result


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (-54, pytest.raises(ValueError)),
                             ("str", pytest.raises(TypeError)),
                             (None, pytest.raises(TypeError))
                         ])
def test_deposit_negative(value, extend_result):
    acc = BankAccount()
    with extend_result:
        assert acc.deposit(value) is None
        assert acc.get_balance() == extend_result


@pytest.mark.bank_account
@pytest.mark.parametrize("value, extend_result",
                         [
                             (0, 0),
                             (2432902008176640000, 2432902008176640000)
                         ])
def test_deposit_boundary(value, extend_result):
    acc = BankAccount()

    assert acc.deposit(value) is None
    assert acc.get_balance() == extend_result
