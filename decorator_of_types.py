def typed(expected_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if isinstance(args, expected_type) is False:
                    args = [expected_type(arg) for arg in args]
            return func(*args)
        return wrapper
    return decorator


@typed(expected_type=str)
def add_1(a, b):
    return a + b


print(add_1("3", 5))
print(add_1(5, 5))
print(add_1("a", "b"))


@typed(expected_type=int)
def add_2(a, b, c):
    return a + b + c


print(add_2(5, 6, 7))


@typed(expected_type=float)
def add_3(a, b, c):
    return a + b + c


print(add_3(0.1, 0.2, 0.4))
