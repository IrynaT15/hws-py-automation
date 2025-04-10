def sum_of_numbers_in_range(number):
    list_of_numbers = [n for n in range(1,number+1)]
    return sum(list_of_numbers)


print(sum_of_numbers_in_range(1))
print(sum_of_numbers_in_range(8))
print(sum_of_numbers_in_range(22))
print(sum_of_numbers_in_range(100))
