from src.practice_1.Calculator import Calculator
import pytest


calculator = None


@pytest.fixture()
def precondition(scope="session"):
    global calculator

    calculator = Calculator()


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             (10, 5, 2),
                             (10, 3, 3.3333333333333335),
                             (6.05, 1.1, 5.499999999999999),
                             (-10, -2, 5),
                             (-5, 2.5, -2)
                         ])
def test_multiply_positive(value_left, value_right, expend_result, precondition):
    global calculator

    assert calculator.divide(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             (10, 1, 10),
                             (5, 5, 1),
                             (0, 54, 0)
                         ])
def test_multiply_boundary(value_left, value_right, expend_result, precondition):
    global calculator

    assert calculator.divide(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             ("str_1", "str_2", pytest.raises(TypeError)),
                             (5, 0, pytest.raises(ValueError)),
                         ])
def test_multiply_negative(value_left, value_right, expend_result, precondition):
    global calculator
    with expend_result:
        assert calculator.divide(value_left, value_right) == expend_result