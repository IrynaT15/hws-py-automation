def typed(type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if type(arg) != type:
                    args = [type(arg) for arg in args]
            return func(*args)
        return wrapper
    return decorator


@typed(type=str)
def add(a, b):
    return a + b


print(add("3", 5))
print(add(5, 5))
print(add("a", "b"))

@typed(type=int)
def add(a, b, с):
    return a + b + с


print(add(5, 6, 7))

@typed(type=float)
def add(a, b, с):
    return a + b + с


print(add(0.1, 0.2, 0.4))
