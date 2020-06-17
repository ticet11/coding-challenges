import functools

def exponenter(base, exponent):
    base_array = []
    rangeNum = range(exponent)
    for num in rangeNum:
        base_array.append(base)
    return functools.reduce(lambda a, b : a * b, base_array)

print(exponenter(10, 2))