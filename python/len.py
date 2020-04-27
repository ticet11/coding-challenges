from functools import reduce
some_string = 'potatoes'

# def length_of_string(string):
#     length = 0
#     for char in string:
#         length += 1

#     print(length)

# length_of_string(some_string)


def length_of_string(string):
    print(reduce(lambda x, y: x + 1, string, 0))


length_of_string(some_string)
