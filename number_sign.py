def find_and_remove_previous(string):

    if "#" not in string:
        return string

    string = list(string)
    i = string.index("#")

    if i == 0:
        string.pop(i)
    else:
        string.pop(i)
        string.pop(i-1)

    string = "".join(string)
    return find_and_remove_previous(string)


print(find_and_remove_previous("a#bc#d"))
print(find_and_remove_previous("abc#d##c"))
print(find_and_remove_previous("abc##d######"))
print(find_and_remove_previous("#######"))
print(find_and_remove_previous(""))
