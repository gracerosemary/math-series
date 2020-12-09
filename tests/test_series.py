from math_series.series import fibonacci

def test_one():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

def test_five():
    actual = fibonacci(5)
    expected = 3
    assert actual == expected

def test_eight():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def test_zero():
    actual = fibonacci(0)
    # expected = 'Nope.'
    assert actual == None