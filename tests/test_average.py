import pytest
from src.main_2 import average


@pytest.mark.parametrize("value, expend_result",
                         [
                             ([1, 6, 4, 87, 34], 26.4),
                             ([-5, -1, -86, -5], -24.25),
                             ([-5, -2, -65, 93, 2], 4.6)
                         ])
def test_average_positive(value, expend_result):
    assert average(value) == expend_result


@pytest.mark.parametrize("value, expend_result",
                         [
                             ("str", TypeError())
                         ])
def test_average_negative(value, expend_result):
    assert average(value) == expend_result


@pytest.mark.parametrize("value, expend_result",
                         [
                             ([], ValueError()),
                             ([i for i in range(5000)], 2499.5),
                             ([68], 68)
                         ])
def test_average_boundary(value, expend_result):
    assert average(value) == expend_result
