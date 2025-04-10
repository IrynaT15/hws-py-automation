def process_line(string, num):
    return string[:num-1] + string[:num][::-1]


print(process_line("abcdef", 1))
print(process_line("abcdef", 2))
print(process_line("abcdef", 3))
print(process_line("abcdef", 4))
