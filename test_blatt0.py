from blatt0 import mybin, myint
from blatt0 import is_palindrome, pascal, flatten, solve_equation, fizz_buzz
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
    assert fizz_buzz(2) == [1, 2]
    assert fizz_buzz(4) == [1, 2, 'fizz', 4]
    assert fizz_buzz(8) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8]
    assert fizz_buzz(9) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz']
    assert fizz_buzz(33) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8,
                             'fizz', 'buzz', 11, 'fizz', 13, 14,
                             'fizzbuzz', 16, 17, 'fizz', 19, 'buzz',
                             'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz',
                             28, 29, 'fizzbuzz', 31, 32, 'fizz']


def test_solve_equation():
    assert solve_equation(1, 1, 1) == {}
    assert solve_equation(2, 4, -2.5) == {-2.5, 0.5}
    assert solve_equation(0, 1, 1) == {-1}


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
