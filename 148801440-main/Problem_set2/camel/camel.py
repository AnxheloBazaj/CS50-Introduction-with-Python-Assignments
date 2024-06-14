def main():
    camelCase = input("camelCase: ") # prompt the user for input in camelCcase
    snake_case = '' #empty string variable which will hold the new string value
    for char in camelCase: # iterate over the users input
        if char.islower(): # if the value of char is lowercase then add to emty variable
            snake_case += char

        elif char.isupper(): # if the value of char is uppercase then convert to lowercase and add underscore before them
            snake_case += '_' + char.lower()


    print(snake_case) # Print the variable which hold the snake_case verion of users input

main() # call main
