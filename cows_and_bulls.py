""" Generate the Secret number: random, 4-digit, non-repeating"""
import random
n1 = str(random.randint(1, 9))
number = [n1]
while len(number) < 4:
    n = str(random.randint(0, 9))
    if n not in number:
        number.append(n)
secret_number = "".join(number)
# print("Secret number:", secret_number)

print("Try to guess the secret number!\n"
      "Remember!\nThe number should consist "
      "only of 4 non-repeating digits.\nGood luck!")

winner = 0
while winner == 0:
    gamer_number = input("Enter your number: ")
    if (len(gamer_number) == 4 and gamer_number.isdigit() and
       len(gamer_number) == len(set(gamer_number))):
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
            print(f"Your result: {cow} cows, {bull} bulls")
            winner = 0
    else:
        print("Invalid number.")

print("You won!")
