from src.practice_1.User import User
import pytest


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("qwe", 22, 22),
                             ("qwe", 66, 66)
                         ])
def test_get_age_positive(name, age, expend_result):
    user = User(name, age)

    assert user.get_age() == expend_result
