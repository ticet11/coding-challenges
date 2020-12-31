email = "hello, my name is brian and the name of my daughter is Daisy."
stripped_email = ""
word_list = []
word_count_dic = {}

# Tokenization
def tokenizer():
    stripped_email = email
    word_repeat_count = 1
    for char in "?,.!/;:": stripped_email = stripped_email.replace(char, "")
    word_list = stripped_email.split()
    for word in word_list: # TODO: fill word_count_dic
    

tokenizer()


