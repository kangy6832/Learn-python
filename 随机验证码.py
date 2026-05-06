import random
import string 

ALL_CHARS = string.ascii_letters + string.digits

def generate_code(*, code_len=4):
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for i in range(10):
    print(generate_code(code_len=6))