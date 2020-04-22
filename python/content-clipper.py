"""
remove_first_and_last(list_to_clean)

html = ['<h1>, 'Some content', '</h1>']

remove_first_and_last(html)
-> ['Some content']

html_2 = ['<h1>, 'Some content', 'More '</h1>']

remove_first_and_last(html_2)
-> ['Some content', 'More']
"""


def content_clipper(content):
    if len(content) < 3:
        print("You're going to decimate this list! Try a larger one.")
    else:
        del content[-1]
        del content[0]
        print(content)


content_clipper([1, 2, 3])


# example given

def remove_first_and_last(content_to_edit):
    _, *content, _ = content_to_edit
    print(content)


remove_first_and_last([1, 2, 3])