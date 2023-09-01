import random
import string

from django.core.cache import cache


def generate_random_string():
    token = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(10)
    )
    cache.set(token, token)
    return token


def get_and_delete_from_cache(key):
    """cache.delete(key)"""

    return cache.get(key)
