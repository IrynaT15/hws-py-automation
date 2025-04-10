def get_square_of_number():
    num = input("Enter your number:")
    return int(num) ** 2


def is_even_number():
    num = input("Enter your number:")
    if int(num) % 2 == 0:
        return f"{num} is even"
    else:
        return  f"{num} is odd"


print(get_square_of_number())
print(is_even_number())
