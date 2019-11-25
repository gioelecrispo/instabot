from instabot.list_utils import commons, diff
from instabot.random_utils import choose_random


def test_list_diff():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6]
    result = diff(list1, list2)
    assert result == [1, 2, 3]


def test_list_commons():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6]
    result = commons(list1, list2)
    assert result == [4, 5]


def test_choose_random():
    list1 = [1, 2, 3, 4, 5]
    result_k_minor_to__list_len = choose_random(list1, k=2)
    assert len(result_k_minor_to__list_len) == 2
    result_k_major_to__list_len = choose_random(list1, k=10)
    assert len(result_k_major_to__list_len) == len(list1)
    result_integer = choose_random(list1)
    assert type(result_integer) == int
