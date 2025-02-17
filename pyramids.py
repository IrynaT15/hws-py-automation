N = 5
n = 0
i = 1
num_chr = 1+(N-1)*2
while n < N:
    pyramid = "*"*i
    n+=1
    i=i+2
    print(pyramid.center(num_chr))
