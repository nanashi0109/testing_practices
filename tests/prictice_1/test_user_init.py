from src.practice_1.User import User
import pytest


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("IG", 22, User("IG", 22))
                         ])
def test_init_positive_1(name, age, expend_result):
    user =  User(name, age)

    assert user.get_age() == expend_result.get_age() and user.get_name() == expend_result.get_name()


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("qwe", 5,  2)
                         ])
def test_init_positive_2(name, age, expend_result):
    user_1 = User(name, age) == expend_result
    user_2 = User(name, age) == expend_result

    User.count == expend_result


@pytest.mark.user
@pytest.mark.parametrize("name, age, expend_result",
                         [
                             ("", 22, pytest.raises(ValueError)),
                             ("qwe", -1, pytest.raises(ValueError)),
                             ("qwe", 200, pytest.raises(ValueError)),
                             ("qwe", 0, pytest.raises(ValueError)),
                             ("qwe", "greater than 1", pytest.raises(TypeError)),
                             ("qwe", 5.2, pytest.raises(TypeError))
                         ])
def test_init_positive(name, age, expend_result):
    with expend_result:
        User(name, age) == expend_result
