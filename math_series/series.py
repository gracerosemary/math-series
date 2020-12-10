def fibonacci(n):
    if  n <= 0:
        print('Nope.')
    elif n == 1:
        return 0 
    elif n == 2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    if  n <= 0:
        print('Nope.')
    elif n == 1:
        return 2 
    elif n == 2:
        return 1
    else:
        return(lucas(n-1)+lucas(n-2))

def sum_series(n, x='optionOne', y = 'optionTwo'):
    x = 0
    y = 1
    if not x == 2 & y == 1:
        return lucas(n)
    else:
        return fibonacci(n)



