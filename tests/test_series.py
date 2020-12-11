import unittest
from math_series.series import fibonacci, lucas, sum_series

# fibonacci tests for 0, 1, 5, 8
def test_zero_fib():
    actual = fibonacci(0)
    expected = None
    assert actual == expected

def test_one_fib():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

def test_five_fib():
    actual = fibonacci(5)
    expected = 3
    assert actual == expected

def test_eight_fib():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected


# lucas tests for 0, 1, 5, 8
def test_zero_lucas():
    actual = lucas(0)
    expected = None
    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 2
    assert actual == expected

def test_five_lucas():
    actual = lucas(5)
    expected = 7
    assert actual == expected

def test_eight_lucas():
    actual = lucas(8)
    expected = 29
    assert actual == expected

# sum series tests for fib
def test_optionals_fib_zero():
    actual = sum_series(0)
    expected = None
    assert actual == expected

def test_optionals_fib_one():
    actual = sum_series(1)
    expected = 0
    assert actual == expected

def test_optionals_fib_five():
    actual = sum_series(5)
    expected = 3
    assert actual == expected

def test_optionals_fib_eight():
    actual = sum_series(8)
    expected = 13
    assert actual == expected

# sum series tests for lucas
def test_optionals_lucas_zero():
    actual = sum_series(0)
    expected = None
    assert actual == expected

def test_optionals_lucas_one():
    actual = sum_series(1, 2, 1)
    expected = 2
    assert actual == expected

def test_optionals_lucas_five():
    actual = sum_series(5, 2, 1)
    expected = 7
    assert actual == expected

def test_optionals_lucas_eight():
    actual = sum_series(8, 2, 1)
    expected = 29
    assert actual == expected

# sum series tests for different series
def test_optionals_different_series():
    actual = sum_series(3, 1, 1)
    expected = 'different series'
    assert actual == expected

