import inflect  # import inflect module


def main():  # define main method
    my_names = []  # empty list which will hold the names later on

    while True:  # infinite loop to keep promptin the user
        try:  #  try statement
            names = input("Name: ")  # prompt the user for names
            my_names.append(names)  # add the names to the emty list

        except EOFError:  # exception handling for EOFError
            if len(my_names) == 0:
                # if the list is empty ignore the error and keep prompting
                print()  # move the user cursor on a new line
                pass
            else:  # an else statement to break out of loop if names were given
                print()  # move the user cursor on a new line
                break

    adieu = inflect.engine().join((my_names))
    # join the names stored in the my_names list into a single string
    print("Adieu, adieu, to", adieu)  #  bid adieu to those names


main()  # call main
