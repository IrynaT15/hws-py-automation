import re


def find_dates_in_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
        dates = re.findall(r"\d{2}\.\d{2}\.\d{4}", text)
        return dates


# print(find_dates_in_file(r'C:\Users\Iryna\hw_3\test\re_dates.txt'))


def write_file_for_testing(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("1.11.1111, 22.22.2222, 12.JN.2020 33,33,3333, 44/44/4444, "
                   "55.55.5555 6666.66.66 10.10.101o 00.00.0000")


# file_path = "test_find_dates_in_file.txt"
# write_file_for_testing(file_path)
# print(find_dates_in_file(file_path))
