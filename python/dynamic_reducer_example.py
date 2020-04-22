"""
import operator
from functools import reduce

dynamic_reducer([1, 2, 3], '+') -> 6
dynamic_reducer([1, 2, 3], '-') -> -4
dynamic_reducer([1, 2, 3], '*') -> 6
dynamic_reducer([1, 2, 3], '/') -> 0.1666666667
"""

import operator
from functools import reduce


def dynamic_reducer(collection, op):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)
    # return reduce(operators[op], collection)

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))
