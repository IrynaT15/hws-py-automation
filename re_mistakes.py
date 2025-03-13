import re


def correct_mistakes(text):
    text = re.sub(r"(\w+)\s+\1", r"\1", text)
    return text


text1 = ("Довольно распространённая ошибка ошибка — "
        "это лишний повтор повтор слова слова. "
        "Смешно, не не правда ли? Не нужно портить хор хоровод.")

print(correct_mistakes(text1))
