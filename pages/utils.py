import random
import string


def random_num():
    """Generates random number"""
    return str(random.randint(111111, 999999))


def random_str(length=7):
    """Generates random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
