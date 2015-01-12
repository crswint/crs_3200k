def adder(x, y):
    ''' Add two integers x and y and display the results

    >>> adder(2, 3)
    5

    '''

    return x + y

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
