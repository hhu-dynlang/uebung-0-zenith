#from blatt0 import pascal
#from blatt0 import flatten
#from blatt0 import fizz_buzz
#from blatt0 import solve_equation
#from blatt0 import myint, mybin
import random

def test_pascal():
    pass # TODO

def test_flatten():
    pass # TODO

def test_fizz_buzz():
    pass # TODO

def test_solve_equation():
    pass # TODO

def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)

def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i

# TODO: more tests