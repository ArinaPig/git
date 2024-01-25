def decorator(func):
    def wrapper(v0, v, t):
        func(0, 10, 5)
        s = (v + v0) / 2 * t
        return s
    return wrapper


@decorator
def func(v0, v, t):
    a = (v - v0) / t
    return a


print(func(0, 10, 5))
