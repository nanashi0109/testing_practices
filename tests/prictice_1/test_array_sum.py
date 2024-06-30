from src.practice_1.Array import Array
import pytest


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([2, 5, 3, 6], 16),
                             ([2.5, 6.3, 1.2, 9.4], 19.4),
                             ([-5, -2, -6, -2, -8], -23),
                             ([-5, 6, -1, 53, -65, 9], -3),
                             ([5, -5.3, 7, 9.1, -6.9], 8.9),
                         ])
def test_sum_positive(value_array, expend_result):
    arr = Array(value_array)

    assert arr.sum() == expend_result


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
        assert arr.sum() == expend_result


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([], None),
                             ([i for i in range(5000)], 12497500)
                         ])
def test_sum_positive(value_array, expend_result):
    arr = Array(value_array)

    assert arr.sum() == expend_result
