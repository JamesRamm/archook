import random
import string

def generate_token():
    length = random.randint(5, 10)
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return token

total_cents = 46
cents_per_token = 0.01

tokens_needed = total_cents // cents_per_token

tokens = [generate_token() for _ in range(tokens_needed)]

print(tokens)
