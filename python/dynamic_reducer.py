"""
import operator
from functools import reduce

dynamic_reducer([1, 2, 3], '+') -> 6
dynamic_reducer([1, 2, 3], '-') -> -4
dynamic_reducer([1, 2, 3], '*') -> 6
dynamic_reducer([1, 2, 3], '/') -> 0.1666666667
"""


def dynamic_reducer(num_list, operator):
    if operator == '+':
        solution = num_list[0]
        for num in range(1, len(num_list)):
            solution += num_list[num]

    elif operator == '-':
        solution = num_list[0]
        for num in range(1, len(num_list)):
            solution -= num_list[num]

    elif operator == '*':
        solution = num_list[0]
        for num in range(1, len(num_list)):
            solution *= num_list[num]

    elif operator == '/':
        solution = num_list[0]
        for num in range(1, len(num_list)):
            solution /= num_list[num]

    print(solution)


dynamic_reducer([1, 2, 3], '+')
dynamic_reducer([1, 2, 3], '-')
dynamic_reducer([1, 2, 3], '*')
dynamic_reducer([1, 2, 3], '/')
