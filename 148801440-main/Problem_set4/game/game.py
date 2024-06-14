import random # import random module


def main(): # define main
    while True: # loop until user inputs valid level
        try:
            level = int(input("Level: ")) # prompt the user and store the value
        except ValueError: # handle the error
            continue
        if level <= 0: # check if the level is valid
            continue
        else:
            break

    rand_int = random.randint(1, level) # generate a random integer and store it

    while True: # loop until user enters the correct guess
        try:
            guess = int(input("Guess: ")) # prompt the user for the guess
        except ValueError: # handle the error
            continue
        if guess < 0: #if the guess is negattive ignore it
            continue
        elif guess > rand_int: #  if guess to large print the message
            print("Too large!")
        elif guess < rand_int: # if guess too small print the message
            print("Too small!")
        else:                   # if the guess is correct print the message
            exit("Just right!")


main() # call main
