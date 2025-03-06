import random
import string

class Utils:
    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
        return f"{random_string}@example.com"
