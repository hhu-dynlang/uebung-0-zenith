#from blatt0 import fizz_buzz
#from blatt0 import solve_equation
#from blatt0 import myint, mybin
from blatt0 import is_palindrome, pascal, flatten
import random


def test_pascal():
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
                         [1, 5, 10, 10, 5, 1]]
    assert pascal(0) == [[1]]
    assert pascal(-1) == []


def test_flatten():
    assert flatten([1, [2]]) == [1, 2]
    assert flatten([[2, 3], 1, [4]]) == [2, 3, 1, 4]
    assert flatten([[2], [3, [4, [5]]]]) == [2, 3, 4, 5]


def test_fizz_buzz():
    assert 4 == 15


def test_solve_equation():
    assert 17 < 4


def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)


def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i


def test_is_palindrome():
    assert is_palindrome('lol') is True
    assert is_palindrome('lolz') is False
    assert is_palindrome('lool') is True
    assert is_palindrome('lo3ol') is True
    assert is_palindrome('lodzudol') is False
