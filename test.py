# Using the with statement
with open('static/secret_key.txt', 'r') as file:
    content = file.read()
    print(content)