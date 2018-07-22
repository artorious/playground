""" Simple calculator """


def add(val1, val2):
    """ 
    Add val1 to val2 and return result 

    >>> add(1, 2)
    3
    >>> add(-1, 10)
    9
    >>> add('a', 'b')
    'ab'
    >>> add(1, '2')
    Traceback (most recent call last):
      File "test.py", line 17, in <module>
        add(1, '2')
      File "test.py", line 14, in add
        return a + b
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return val1 + val2

def subtract(val1, val2):
    """
    Returns the result of subtracting val2 from val2

    >>> subtract(2, 1)
    1
    >>> subtract(10, 10)
    0
    >>> subtract(7, 10)
    -3
    """
    return val1 - val2

