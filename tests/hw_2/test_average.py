import pytest
from src.hw_2.main_2 import average


@pytest.mark.parametrize("value, expected_result",
                         [
                             ([1, 6, 4, 87, 34], 26.4),
                             ([-5, -1, -86, -5], -24.25),
                             ([-5, -2, -65, 93, 2], 4.6),
                             ([1.5, 5.2, 6.42, -7.6], 1.38),
                             ([1, 5.3, -5, -6.32], -1.255)
                         ])
def test_average_positive(value, expected_result):
    assert average(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             ("str", pytest.raises(TypeError))
                         ])
def test_average_negative(value, expected_result):
    with expected_result:
        assert average(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             ([i for i in range(5000)], 2499.5),
                             ([68], 68)
                         ])
def test_average_boundary_1(value, expected_result):
    assert average(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             ([], pytest.raises(ValueError)),
                         ])
def test_average_boundary_2(value, expected_result):
    with expected_result:
        assert average(value) == expected_result
