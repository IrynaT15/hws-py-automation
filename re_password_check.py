import re


def check_password(password):
    if (len(password) >= 4 and
        re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("\d", password)):
        return f"{password} Good password"
    return f"{password} Bad password"


# print(check_password("abC!1"))
# print(check_password("aC 1"))
# print(check_password("AAAA"))
# print(check_password("aaaa"))
# print(check_password("1234"))
# print(check_password("123a"))
# print(check_password("123A"))
# print(check_password("AAa"))
# print(check_password("Aa"))
# print(check_password("A"))
# print(check_password("a"))
# print(check_password(""))

password = input("Enter your password to check if it's correct: ")
print(check_password(password))
