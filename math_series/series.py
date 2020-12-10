def fibonacci(n):
    if  n <= 0:
        print('Nope.')
    elif n == 1:
        return 0 
    elif n == 2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

def lucas(n):
    if  n <= 0:
        print('Nope.')
    elif n == 1:
        return 2 
    elif n == 2:
        return 1
    else:
        return (lucas(n-1)+lucas(n-2))

def sum_series(n, x = 'optionOne', y = 'optionTwo'):
    
    optionalArgs = [
        x == 2,
        y == 1
        ]
        
    invertArgs = [
        x == 1,
        y == 2,
        ]
        
    diffSeries = [
        x != 2,
        y != 1
        ]

    if all(optionalArgs):
        return lucas(n)
    elif not any(invertArgs) and any(diffSeries) and not any(optionalArgs):
        return fibonacci(n)
    elif any(invertArgs) or any(diffSeries):
        return "different series"