import string
import random

def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))