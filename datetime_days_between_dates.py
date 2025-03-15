# Создайте программу, которая будет запрашивать у пользователя
# две даты в формате "ГГГГ-ММ-ДД".
# Вычислите и выведите на экран количество дней между этими датами.
# Подсказка: используйте функцию relativedelta из модуля dateutil.

from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from datetime import datetime, date


def count_and_display_number_of_days_between_dates(date_first, date_second):
    dt_1 = parse(date_first)
    dt_2 = parse(date_second)
    diff = dt_2 - dt_1
    return diff.days


date1 = input("Enter Date One (YYYY-MM-DD):")
date2 = input("Enter Date Two (YYYY-MM-DD):")
a = count_and_display_number_of_days_between_dates(date1, date2)
print(a)
