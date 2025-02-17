""" Generate the Secret number: random, 4-digit, non-repeating"""
import random
n1 = str(random.randint(1, 9))
secret_number = [n1]
while len(secret_number) < 4:
    n = str(random.randint(0, 9))
    if n not in secret_number:
     secret_number.append(n)
secret_number = "".join(secret_number)

print("Secret number:", secret_number)

gamer_number = input("Enter your number: ")
validation = 0

while validation == 0:
    if len(gamer_number) == 4:
        if gamer_number.isdigit():
            if (gamer_number[0] in gamer_number[1:] or
                gamer_number[1] in gamer_number[2:] or
                gamer_number[2] == gamer_number[3]):
                print("The number should consist of non-repeating digits.")
                gamer_number = input("Enter your number: ")
            else:
                 if int(gamer_number) == int(secret_number):
                     print("You won!")
                     print("Secret number is ", secret_number)
                     validation = 1
                 else:
                     secret_number_list = [int(x) for x in secret_number]
                     gamer_number_list = [int(x) for x in gamer_number]
                     bull = 0
                     cow = 0
                     for x in gamer_number_list:
                         for y in secret_number_list:
                             if x == y and gamer_number_list.index(x) == secret_number_list.index(y):
                                 bull += 1
                             elif x == y and gamer_number_list.index(x) != secret_number_list.index(y):
                                 cow += 1
                     if cow != 1 and bull != 1:
                         print(cow, "cows, ", bull, "bulls")
                     elif cow == 1 and bull != 1:
                         print(cow, "cow, ", bull, "bulls")
                     elif cow != 1 and bull == 1:
                         print(cow, "cows, ", bull, "bull")
                     bull = 0
                     cow = 0
                     print("Try again!")
                     gamer_number = input("Enter your number: ")
                     validation = 0
        else:
            print("The number should consist only of digits.")
            validation = 0
            gamer_number = input("Enter your number: ")
    else:
        print ("The number should consist of 4 digits.")
        validation = 0
        gamer_number = input("Enter your number: ")
