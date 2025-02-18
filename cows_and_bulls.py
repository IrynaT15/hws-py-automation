""" Generate the Secret number: random, 4-digit, non-repeating"""
import random
n1 = str(random.randint(1, 9))
secret_number = [n1]
while len(secret_number) < 4:
    n = str(random.randint(0, 9))
    if n not in secret_number:
        secret_number.append(n)
secret_number = "".join(secret_number)
#print("Secret number:", secret_number)

print("""Try to guess the secret number!
Remember! The number should consist only of 4 non-repeating digits.
Good luck!""")
gamer_number = input("Enter your number: ")

winner = 0
while winner == 0:
    if len(gamer_number) == 4:
        if gamer_number.isdigit():
            for i in gamer_number:
                if gamer_number.count(i) == 1:
                    True
                else:
                    print("The number should consist of non-repeating digits.")
                    winner = 0
                    gamer_number = input("Enter your number: ")
            if gamer_number == secret_number:
                winner = 1
            else:
                secret_number_list = [int(x) for x in secret_number]
                gamer_number_list = [int(x) for x in gamer_number]
                bull = 0
                cow = 0
                for x in gamer_number_list:
                    for y in secret_number_list:
                        if x == y:
                            if gamer_number_list.index(x) == secret_number_list.index(y):
                                bull += 1
                            else:
                                cow += 1
                        if cow == 1:
                            c = "cow"
                        else:
                            c = "cows"

                        if bull == 1:
                            b = "bull"
                        else:
                            b = "bulls"
                print(cow, c, bull, b)
                bull, cow = 0, 0
                print("Try again!")
                gamer_number = input("Enter your number: ")
                winner = 0
        else:
            print("The number should consist only of digits.")
            winner = 0
            gamer_number = input("Enter your number: ")

    else:
        print("The number should consist of 4 digits.")
        winner = 0
        gamer_number = input("Enter your number: ")

print("You won!")
