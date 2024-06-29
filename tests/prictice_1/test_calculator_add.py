from src.practice_1.Calculator import Calculator
import pytest


calculator = None


@pytest.fixture
def precondition(scope="session"):

    global calculator
    calculator = Calculator()


@pytest.mark.calculator
@pytest.mark.parametrize("left_value, right_value, expend_result",
                         [
                             (2, 5, 7),
                             (2.5, 5.2, 7.7),
                             (-5, -8, -13),
                             (-6.5, -2.5, -9)
                         ])
def test_add_positive(left_value, right_value, expend_result, precondition):
    global calculator

    assert calculator.add(left_value, right_value) == expend_result


@pytest.mark.calculator
@pytest.mark.parametrize("left_value, right_value, expend_result",
                         [
                             ("str_1", "str_2", pytest.raises(TypeError)),
                             ("5", "7", pytest.raises(TypeError)),
                             ([5], [7], pytest.raises(TypeError)),
                         ])
def test_add_negative(left_value, right_value, expend_result, precondition):
    global calculator
    with expend_result:
        assert calculator.add(left_value, right_value) == expend_result
