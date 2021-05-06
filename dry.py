# DRY - don't repeat yourself

# winning_number = 43
# guess = 1
# number = int(input("Guess number between 1 to 100: "))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"You win, and you guess this number in {guess} times")
#         game_over = True
#     else:
#         if number < winning_number :
#             print("too low")

#         else :
#             print("too high")

#         guess += 1
#         number = int(input("guess again: "))

# for ramdom number
import random
winning_number = random.randint(1,100)

# for set number
# winning_number = 43
guess = 1
number = int(input("Guess number between 1 to 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win, and you guess this number in {guess} times")
        game_over= True
    else:
        if number < winning_number :
            print("too low")

        else :
            print("too high")

        guess += 1
        number = int(input("guess again: "))