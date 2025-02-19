N = 10  # Number of rows
n = 0   # Rows counter
i = 1   # Stars counter
num_chr = 1+(N-1)*2  # Number of characters in the row
while n < N:
    pyramid = "*" * i
    n += 1
    i += 2
    print(pyramid.center(num_chr))
