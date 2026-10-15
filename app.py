
def add_numbers(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be a number")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be a number")

    return a + b


def divide_numbers(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be a number")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be a number")

    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")

    return a / b
