def is_palindrom(char):
    return str(char) == str(char)[::-1]


print(is_palindrom(12321))
print(is_palindrom(123))
print(is_palindrom("alla alla"))
print(is_palindrom("alla lala"))
