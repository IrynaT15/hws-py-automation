def letters_count(string):
    string_new = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        elif count > 1:
            string_new.append(string[i - 1] + str(count))
            count = 1
        else:
            string_new.append(string[i - 1])
            count = 1

    string_new.append(string[-1])
    if count > 1:
        string_new.append(str(count))

    return ''.join(string_new)


print(letters_count("cccbba"))
print(letters_count("abeehhhhhccced"))
print(letters_count("aaabbceedd"))
print(letters_count("abcde"))
print(letters_count("aaabbdefffff"))
