"""
heading_generator(title, heading_type)

heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Howdy', '3')
<h3>Howdy<h3>
"""
content_example = 'Hello'
tag_example = 'h'

def html_content_generator(content, tag):
  if tag.lower() == 'h':
    heading_number = input('Which heading number?')
    print(f'<{tag}{heading_number}>{content}<{tag}{heading_number}>')
  else:
    print(f'<{tag}>{content}<{tag}>')

html_content_generator(content_example, tag_example)