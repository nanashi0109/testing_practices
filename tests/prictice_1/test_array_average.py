from src.practice_1.Array import Array
import pytest


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([2, 5, 3, 6], 4),
                             ([2.5, 6.3, 1.2, 9.4], 4.86),
                             ([-5, -2, -6, -2, -8], -4.6),
                             ([-5, 6, -1, 3, -2, 9], 2),
                             ([5, -5.3, 7, 9.1, -6.9], 1.78),
                         ])
def test_sum_positive(value_array, expend_result):
    arr = Array(value_array)

    assert arr.average() == expend_result


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (None, pytest.raises(TypeError)),
                             (["123", True, None], pytest.raises(TypeError))
                         ])
def test_sum_positive(value_array, expend_result):
    arr = Array(value_array)

    with expend_result:
        assert arr.average() == expend_result


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([], None),
                             ([i for i in range(1, 5000, 1)], 2500)
                         ])
def test_sum_positive(value_array, expend_result):
    arr = Array(value_array)

    assert arr.average() == expend_result
