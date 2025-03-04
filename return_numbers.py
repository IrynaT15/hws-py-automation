def decorator(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, (int, float)):
            print(f"Correct. The result {result} is a number.")
        else:
            print(f"Error. The result {result} is not a number.")
        return result
    return wrapper


@decorator
def my_function(a, b):
    return a + b


my_function(23, 56)
my_function("A", "a")
