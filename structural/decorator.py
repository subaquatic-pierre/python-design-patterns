from functools import wraps


def decorate_function(function):
    """Decorate Function"""

    @wraps(function)
    def wrapper():
        val = function()
        new_val = val + " DECORATED"
        return new_val

    return wrapper


@decorate_function
def hello_world():
    """Original Function!"""
    return "Hello, World!"
