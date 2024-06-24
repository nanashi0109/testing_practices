import pytest
from hw_2.src.main_2 import factorial


@pytest.mark.parametrize("value, expected_result",
                         [
                             (5.2, pytest.raises(TypeError)),
                             ("5", pytest.raises(TypeError)),
                             (-3, pytest.raises(ValueError)),
                         ])
def test_factorial_negative(value, expected_result):
    with expected_result:
        assert factorial(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             (10, 3628800)
                         ])
def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             (0, 1),
                             (50, 30414093201713378043612608166064768844377641568960512000000000000)
                         ])
def test_factorial_boundary(value, expected_result):
    assert factorial(value) == expected_result


