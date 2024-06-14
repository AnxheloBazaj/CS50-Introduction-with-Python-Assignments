import random  # import random library


def main():  # define main
    game_logic()  # call the game_logic function


def game_logic():  # define the game_logic function
    dificulty = get_level()  # variable which hold the returned value of the function
    score, attempts = 0, 1  # initialize score and attempts
    # attempts = 1
    for i in range(10):  # loop 10 times to generate 10 problems
        x = generate_integer(dificulty)  # generate a random integer
        y = generate_integer(dificulty)  # generate a random integer
        z = x + y  # calculate the sum and store it in a variable
        while True:  # loop until correct answer
            prompt = f"{x} + {y} = "  # create a prompt for the user
            try:  # try block
                result = int(input(prompt))  # prompt the user for the result
            except ValueError:  # handle the exception
                continue
            if result != z:  # check if the answer is incorrect
                if attempts == 3:  # check the number of attempts
                    print(prompt, z)  # print the correct answer
                    attempts = 1  # reset the nuber of attempts
                    break  # break out of loop
                print("EEE")  # print an error message
                attempts += 1  # increment attempts by 1
                continue
            elif result == z:  # check if the answer is correct
                attempts = 1  # reset the number of attepmts
                score += 1  # increment the score by 1
                break  # break out of loop

    print(f"Score:{score}")  # print the total score


def get_level():  # define get_level function
    while True:  # loop until the correct input is given
        try:
            level = int(input("Level:")) # prompt the user for input
        except ValueError: # handle the error
            continue # if input is invalid continue the loop
        if level != 0 and level <= 3: # check if the input is correct
            return level  # return the input as an integer


def generate_integer(level): # define generate_integer function
    max_range = 0 # initialize  max_range
    min_range = 0 # initialize  min_range
    if level == 1: # if level is 1
        max_range, min_range = 9, 0 # set max and min range
    elif level == 2: # if level is 2
        max_range, min_range = 99, 10 # set  max and min range
    else: # if level is 3
        max_range, min_range = 999, 100 # set max and min range
    return random.randint(min_range, max_range) # return a random integer within the range


if __name__ == "__main__":
    main() # call main
