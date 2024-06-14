def main():
    user_input = input()  #Prompt the user fr input
    converted_input = convert(user_input) #variable that calls the convert function and holds as the value the converted input
    print( converted_input) # print the result

def convert(input_string):  # Create convert function that has one parameter
    converted_string = input_string.replace(":)", "🙂").replace(":(", "🙁") # replace :) and :) with 🙂 and 🙁 via the replace method
    return converted_string


main() #call main and execute the program

# Resources used :  docs.python.org/3/library/functions.html#input
#                   docs.python.org/3/library/stdtypes.html#string-methods.
