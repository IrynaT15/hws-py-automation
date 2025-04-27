def items(*args, **kwargs):
    def decorator(func):
        def wrapper(num):
            print(args, kwargs)
            return func(num)
        return wrapper
    return decorator


@items(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(x):
  return x


print(identity(42))


@items()
def identity(x):
  return x


print(identity(42))
