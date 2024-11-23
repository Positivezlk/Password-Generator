import string
from random import randint

def generate_password():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    result = ''
    for i in range(30):
        result += all_chars[randint(0, len(all_chars) - 1)]
    return result

print(generate_password())
