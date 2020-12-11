def fibonacci(n):
    """Returns None for 0, 0 for 1st sequence, 1 for 2nd sequence, or else returns the nth sequence of the series
    :param integer (nth sequence of series)
    :type integer
    :rtype integer
    """
    return None if n <= 0 else 0 if n == 1 else 1 if n == 2 else (fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    """Returns None for 0, 2 for 1st sequence, 1 for 2nd sequence, or else returns the nth sequence of the series
    :param integer (nth sequence of series)
    :type integer
    :rtype integer
    """
    return None if n <= 0 else 2 if n == 1 else 1 if n == 2 else (lucas(n-1)+lucas(n-2))

def sum_series(n, x = 0, y = 1):   
    """Returns nth sequence of lucas series if all optional args are true, nth sequence of fibonacci if all default args are true, else 'different series'
    :param integer (nth sequence of series), 2nd and 3rd optional
    :type integer
    :rtype integer
    """
    defaultArgs = [x == 0, y == 1]
    optionalArgs = [x == 2, y == 1]
        
    return lucas(n) if all(optionalArgs) else fibonacci(n) if all(defaultArgs) else 'different series' 

# attribution: short circuit eval - https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/