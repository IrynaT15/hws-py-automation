def check_cart_number_Luhn(number):
    if number.isdigit():  # Check that no letters or spaces or special chars
        number_list = list(map(int, list(number)))
        list_1 = []
        list_2 = []
        if (len(number) - 1) % 2 != 0:
            for num in number_list[::2]:
                list_1.append(num)
            for num in number_list[1::2]:
                list_2.append(num)
        else:
            for num in number_list[1::2]:
                list_1.append(num)
            for num in number_list[::2]:
                list_2.append(num)
        sum_num_1 = 0
        for num in list_1:
            if 2 * num > 9:
                num_1 = 2 * num - 9
            else:
                num_1 = 2 * num
            sum_num_1 += num_1
        sum_num_2 = 0
        for num in list_2:
            sum_num_2 += num
        if ((sum_num_1 + sum_num_2) % 10) == 0:
            return True
    return False

number = input("Enter card number: ")
print(check_cart_number_Luhn(number))
