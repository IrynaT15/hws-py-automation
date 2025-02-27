def cache(func):
    cached_values = dict()
    def wrapper(*args):
        if args in cached_values:
            return cached_values[args]
        else:
            value = func(*args)
            cached_values[args] = value
            return value
    return wrapper


@cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
