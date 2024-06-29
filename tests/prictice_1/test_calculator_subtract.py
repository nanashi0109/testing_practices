from src.practice_1.Calculator import Calculator
import pytest


calculator = None


@pytest.fixture
def precondition(scope="session"):

    global calculator
    calculator = Calculator()


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             (7, 5, 2),
                             (5, 7, -2),
                             (5.7, 2.5, 3.2)
                         ])
def test_subtract_positive(value_left, value_right, expend_result, precondition):
    global calculator

    assert calculator.subtract(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             ("str_1", "str_2", pytest.raises(TypeError)),
                             ([7], [2], pytest.raises(TypeError)),
                         ])
def test_subtract_negative(value_left, value_right, expend_result, precondition):
    global calculator

    with expend_result:
        assert calculator.subtract(value_left, value_right) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("value_left, value_right, expend_result",
                         [
                             (5, 5, 0)
                         ])
def test_subtract_boundary(value_left, value_right, expend_result, precondition):
    global calculator

    assert calculator.subtract(value_left, value_right) == expend_result
