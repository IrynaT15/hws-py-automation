import re


def check_password(password):
    if (len(password) >= 4
            and re.search("[A-Z]", password)
            and re.search("[a-z]", password)
            and re.search(r"\d", password)):
        return "Good password"
    return "Bad password"


password1 = input("Enter your password to check if it's correct: ")
print(check_password(password1))


if __name__ == "__main__":
    assert check_password("abC!1") == "Good password"
    assert check_password("aC 1") == "Good password"
    assert check_password("AAAA") == "Bad password"
    assert check_password("aaaa") == "Bad password"
    assert check_password("1234") == "Bad password"
    assert check_password("123a") == "Bad password"
    assert check_password("AAa") == "Bad password"
    assert check_password("Aa") == "Bad password"
    assert check_password("A") == "Bad password"
    assert check_password("a") == "Bad password"
    assert check_password( "") == "Bad password"
