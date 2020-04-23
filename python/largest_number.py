numbers = [5, 2, 6]

def smallest_or_greatest(small_or_great):
    if small_or_great.lower() == 'smallest':
        find_smallest(numbers)
    elif small_or_great.lower() == 'greatest':
        find_greatest(numbers)
    else:
        print('I can only find smallest or greatest')

def find_greatest(number_list):
    highest = 0
    for num in number_list:
        if num > highest:
            highest = num

    print(highest)

def find_smallest(number_list):
    number_list.sort()
    smallest = number_list[0]
    print(smallest)

smallest_or_greatest('greatest')