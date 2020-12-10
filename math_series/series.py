def fibonacci(n):
    return None if n <= 0 else 0 if n == 1 else 1 if n == 2 else (fibonacci(n-1)+fibonacci(n-2))
    
    # if  n <= 0:
    #     return None
    # elif n == 1:
    #     return 0 
    # elif n == 2:
    #     return 1
    # else:
    #     return (fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    return None if n <= 0 else 2 if n == 1 else 1 if n == 2 else (lucas(n-1)+lucas(n-2))
    # if  n <= 0:
    #     return None
    # elif n == 1:
    #     return 2 
    # elif n == 2:
    #     return 1
    # else:
    #     return (lucas(n-1)+lucas(n-2))

def sum_series(n, x = 0, y = 1):   
    defaultArgs = [x == 0, y == 1]
    optionalArgs = [x == 2, y == 1]
        
    return lucas(n) if all(optionalArgs) else fibonacci(n) if all(defaultArgs) else 'different series' 

    # if all(optionalArgs):
    #     return lucas(n)
    # elif all(defaultArgs):
    #     return fibonacci(n)
    # else:
    #     return "different series"


# attribution: short circuit eval - https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/