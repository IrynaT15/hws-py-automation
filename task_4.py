def add_1_to_number_and_return_list(number):
    number += 1
    number_list = list(map(int, str(number)))
    return number_list


print(add_1_to_number_and_return_list(9))
print(add_1_to_number_and_return_list(123))
print(add_1_to_number_and_return_list(119))
print(add_1_to_number_and_return_list(999))
