def how_many_char(string):
    string = string.lower().replace(' ', '').replace(',', '')
    char_dic = {}
    for char in string:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    print(char_dic)

how_many_char('Hello, friend')
    