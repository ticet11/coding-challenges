import requests
from bs4 import BeautifulSoup
"""
- Scrape data from 'http://www.dailysmarty.com/topics/python'
- from the link of each post, retrieve the title and print beautifully.
"""
response = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all(class_='post-link-title')

for post in posts:
    title = str(post.h2.a)
    sep_L = "posts/"
    sep_R = '">'
    title = title.split(sep_L, 1)[1].split(sep_R, 1)[0].replace('-', ' ').title()
    f = open('title.txt', 'a')
    f.write((f'{title}\n'))
f.close()
