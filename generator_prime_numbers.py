# Создайте генераторную функцию,
# которая генерирует все простые числа в заданном диапазоне.
# Выведите первые 10 простых чисел из этого диапазона.


def prime_numbers_generator(start, end):
    not_prime_numbers_list = []
    for number in range(start, end+1):
        if number in(2, 3):
            yield number
        if number > 3:
            for i in range(2, number):
                if number % i == 0:
                    not_prime_numbers_list.append(number)
            if number not in not_prime_numbers_list:
                yield number


prime_numbers = prime_numbers_generator(1, 100)


for _ in range(10):
    print(next(prime_numbers))
