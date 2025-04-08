def generate_numbers_from_1_to_N(quantity):
    number = 0
    quantity = int(quantity)
    while quantity > 0:
        number += 1
        yield number
        quantity -= 1


N = input("Enter number: ")
generator = generate_numbers_from_1_to_N(N)
sum_of_numbers = sum(next(generator) for _ in range(int(N)))
print(sum_of_numbers)
