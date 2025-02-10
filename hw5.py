# Task 1: Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
a = 'www.my_site.com#about'
print("Task 1: ", a.replace("#", "/"))

# Task 2: Напишите программу, которая добавляет ‘ing’ к словам
word = "go"
print("Task 2: ", word + "ing")

words = ["go", "work", "play","undrstand", "laugh"]
for x in words:
    print(x + "ing")

# Task 3: В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
str = "Ivanou Ivan"
str = " ".join(str.split()[::-1])
print("Task 3: ", str)

# Task 4: Напишите программу которая удаляет пробел в начале, в конце строки
str1 = " Alice in the Wonderland "
print("Task 4: ", str1.lstrip())
print("Task 4: ", str1.rstrip())

# Task 5: Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
# "pARiS" >> "Paris"
proper_noun = "pARiS"
print("Task 5: ", proper_noun.capitalize())
print("Task 5: ", proper_noun.title())

# Task 6: Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
str_to_list_1 = "Robin Singh"
print("Task 6: ",type(str_to_list_1.split()), str_to_list_1.split())

# Task 7: "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_to_list_2 = "I love arrays they are my favorite"
print("Task 7: ",type(str_to_list_2.split()), str_to_list_2.split())

# Task 8: Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
list_1 = ["Ivan", "Ivanou"]
str_1 = "Minsk"
str_2 = "Belarus"
print("Task 8: ", "Привет,", list_1[0], list_1[1] + "! ", "Добро пожаловать в ", str_1 , str_2)
print("Task 8: ", "Привет,", " ".join(list_1) + "! ", "Добро пожаловать в {}, {}".format(str_1 , str_2))
print("Task 8: ", "Привет,", " ".join(list_1) + "! ", "Добро пожаловать в {city}, {country}".format(city=str_1, country=str_2))
print("Task 8: ", "Привет,", " ".join(list_1) + "! ", f"Добро пожаловать в {str_1}, {str_2}")

# Task 9: Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list_2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_3 = " ".join(list_2)
print("Task 9: ", type(str_3), str_3)

# Task 10: Создайте список из 10 элементов,
# вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
list_3 = ["Honey", 15, [1, 2, 3], "old 3", 2*2,  "Item 6 To remove", {"a": "b"}, 0, True, "the End"]
print("Task 10: ",list_3)
list_3.insert(3, "new 3")
del list_3[6]
print("Task 10: ",list_3)



