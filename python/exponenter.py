def exponenter(base, exponent):
    total = 1
    for num in range(0, exponent):
        total *= base
    return total

print(exponenter(5, 2))