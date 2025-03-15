# Напишите программу, которая будет логировать информацию о действиях пользователя.
# Логи должны записываться в файл "user_actions.log"
# и содержать время события, уровень логирования и сообщение с описанием действия пользователя.
# Используйте соответствующий уровень логирования в зависимости от типа действия
# (например, INFO для успешных действий и ERROR для ошибок).
#
# Расширьте программу из задания 1 таким образом,
# чтобы логи также выводились на консоль с использованием отдельного обработчика.

import re
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = logging.FileHandler("user_actions.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def start_program():
    start_input = input("Enter START to start the program:").strip()
    while start_input.lower() != "start":
        logger.error("Start failed. Input field: start_input. User input: %s", start_input)
        start_input = input("Enter START to start the program:").strip()
    logger.info("Program started. Input field: start_input. User input: %s", start_input)


def get_user_name():
    user_name = input("Enter your name: ").strip()
    while not user_name:
        logger.warning("Input field: user_name. User name is not provided.")
        user_name = input("Enter your name: ").strip()
    logger.info("Input field: user_name. User name: %s", user_name)
    return user_name


def get_date():
    current_date = input("Enter today's date (YYYY-MM-DD): ").strip()
    match = re.match(r"^\d{4}-\d{2}-\d{2}$", current_date)
    while not match:
        logger.error("Not provided or invalid date."
                     "Input field: current_date. User input: %s", current_date)
        current_date = input("Enter today's date (YYYY-MM-DD): ").strip()
        match = re.match(r"^\d{4}-\d{2}-\d{2}$", current_date)
    logger.info("Input field: current_date. Provided date: %s", current_date)
    return current_date


def get_user_comment():
    user_comment = input("Enter your comment: ").strip()
    while not user_comment:
        logger.warning("Input field: user_comment. User comment is not provided")
        user_comment = input("Enter your comment: ").strip()
    logger.info("Input field: user_comment. User comment: %s", user_comment)
    return user_comment


def save_comment():
    save_input = input("Enter SAVE to save the comment:").strip()
    while not save_input.lower() == "save":
        logger.error(f"Saving failed. Input field: save_input. User input: %s", save_input)
        save_input = input("Enter SAVE to save the comment:").strip()
    logger.info("Comment saved. Input field: save_input. User input: %s", save_input)
    print("Your comment is successfully saved")


start_program()
user_name_1 = get_user_name()
date_1 = get_date()
comment_1 = get_user_comment()
save_comment()

print(f"{user_name_1}, your comment is successfully saved ({date_1})")
