from src.practice_1.User import User
import pytest


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("Laki", 22, "Laki")
                         ])
def test_get_name_positive(name, age, expend_result):
    user = User(name, age)

    assert user.get_name() == expend_result


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             (51, 12, "51")
                         ])
def test_get_name_positive(name, age, expend_result):
    user = User(name, age)

    assert user.get_name() == expend_result
