from functools import reduce

num_list_1 = [0, 50, 100]

# def find_average(num_list):
#     total = 0
#     for num in num_list:
#         total += num
#     average = total / len(num_list)
#     print(average)

# find_average(num_list_1)

# def find_average(num_list):
#     average = sum(num_list) / len(num_list)
#     print(average)

# find_average(num_list_1)


def find_average(num_list):
    average = (reduce(lambda a, b: a + b, num_list) / len(num_list))
    print(average)
    

find_average(num_list_1)
