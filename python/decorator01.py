"""
Example of decorator in which arguments are passed in decorator.
"""

from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

