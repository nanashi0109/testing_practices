from src.practice_1.User import User
import pytest


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("qwe", 98, 99)
                         ])
def test_up_age_positive(name, age, expend_result):
    user = User(name, age)

    assert user.up_age() == expend_result
