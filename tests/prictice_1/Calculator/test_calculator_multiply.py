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
                             (5, 10, 50),
                             (2.5, 5.5, 13.75),
                             (-5, -2, 10),
                             (-5, 2.5, -12.5)
                         ])
def test_multiply_positive(value_left, value_right, expend_result, precondition):
    global calculator

    assert calculator.multiply(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             ("str_1", "str_2", pytest.raises(TypeError)),
                             ("str", 2, pytest.raises(TypeError)),
                         ])
def test_multiply_negative(value_left, value_right, expend_result, precondition):
    global calculator
    with expend_result:
        assert calculator.multiply(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             (5, 5, 25)
                         ])
def test_multiply_boundary(value_left, value_right, expend_result, precondition):
    global calculator
    assert calculator.multiply(value_left, value_right) == expend_result
