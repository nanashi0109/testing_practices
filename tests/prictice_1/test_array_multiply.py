from src.practice_1.Array import Array
import pytest


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([2, 5, 3, 6], 180),
                             ([2.5, 6.3, 1.2, 9.4], 177.66),
                             ([-5, -2, -6, -2, -8], -960),
                             ([-5, 6, -1, 3, -2, 9], -1620),
                             ([5, -5.3, 7, 9.1, -6.9], 11647.545),
                         ])
def test_multiply_positive(value_array, expend_result):
    arr = Array(value_array)

    assert arr.multiply() == expend_result


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (None, pytest.raises(TypeError)),
                             (["123", True, None], pytest.raises(TypeError))
                         ])
def test_multiply_negative(value_array, expend_result):
    arr = Array(value_array)

    with expend_result:
        assert arr.multiply() == expend_result


@pytest.mark.array
@pytest.mark.parametrize("value_array, expend_result",
                         [
                             ([], None),
                             ([i for i in range(1, 250, 1)], 12931425043636430929283258208097473883979374870695122666991769708451294990220444837955271661484112797803714029412757731706923726851235963291164121116285127686706108960757058932872164745044027331701460534715756358279742854120700162052715040308991732261609356024659302208995277746290344229596890565019331928819396550887106602565107435228612515915110691807655963377509914810356691893020601132967149282632753928249914330639235395302195200000000000000000000000000000000000000000000000000000000000)
                         ])
def test_multiply_boundary(value_array, expend_result):
    arr = Array(value_array)

    assert arr.multiply() == expend_result