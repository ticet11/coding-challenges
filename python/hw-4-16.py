###############################################################
# Write a Python program to calculate the length of a string. #
###############################################################

some_string = "zippidy doo da"
print(len(some_string))

##############################################################
# Write a Python program to get a string made of the first 2 #
# and the last 2 chars from a given a string.                #
##############################################################

some_string = "zippidy doo da"
first_two = some_string[0:2]
last_two = some_string[-2:]
print(first_two + last_two)

################
# Extra Credit #
################

some_string = "d"
first_two = some_string[0:2]
last_two = some_string[-2:]
if len(some_string) < 2:
    print('')
else:
    print(first_two + last_two)

################
# Name and Age #
################

name = "Brian"
birth_year = 1993
current_year = 2020
age = (current_year - birth_year)

print(f'Hello, my name is {name} and I am {age} years old')

#########################################
# $ Find and Replace all but first char #
#########################################



def dollar_bills():
    some_string = "dippidy doo da"
    first_char = some_string[0]
    count = 0
    for i in some_string:
        if i == first_char:
            count = count + 1
        
    some_string_reverse = some_string[::-1]
    some_string = some_string_reverse.replace(first_char, '$', count-1)
    print(some_string[::-1])

dollar_bills()

#############
# Residents #
#############

residents = ['Jan', 'Fran', 'Dan', 'Lan', 'Stan']

residents.pop(2)

residents.append('Flan')

residents.sort()

print(residents)