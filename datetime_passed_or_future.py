from datetime import datetime, date


def check_if_date_is_future(date_to_check):
    date_full = datetime.strptime(date_to_check, '%Y-%m-%d')
    date_ymd = datetime.date(date_full)
    current_date = date.today()
    if date_ymd < current_date:
        return f"{date_to_check} is a passed date. Current date is {current_date}"
    elif date_ymd > current_date:
        return f"{date_to_check} is a future date. Current date is {current_date}"
    return f"{date_to_check} is today"


date3 = input("Enter Date (YYYY-MM-DD):")
b = check_if_date_is_future(date3)
print(b)
