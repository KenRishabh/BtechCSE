#MODIFY NUMBER GUESSING GAME
winning_number = 43
guess = 1
number = int(input("Guess number between 1 to 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win, and you guess this number in {guess} times")
        game_over = True
    else:
        if number < winning_number :
            print("too low")
            guess += 1
            number = int(input("guess again: "))
        else :
            print("too high")
            number = int(input("guess again: "))
