def letter_search(some_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    binary_output = ''
    for char in alphabet:
        if char in some_string.lower():
            binary_output += '1'
        else:
            binary_output += '0'
    return binary_output

print(letter_search('Abc'))
            

