def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("All arguments should be positive.")
        func(*args)
        print("All arguments are positive.")
    return wrapper


@validate_arguments
def my_function(*args):
    print(args)


my_function(1, 12, 3)
my_function(1, 12, -33)
my_function(1, 12, 3, 0)
