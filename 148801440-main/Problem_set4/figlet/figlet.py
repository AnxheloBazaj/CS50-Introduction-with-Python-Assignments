import sys  # import sys module
from pyfiglet import Figlet  # import Figlet from pyfiglet module
import random  # import random module


def main():  # define main
    options = ["-f", "--font"]  # list of options
    figlet = Figlet()  # create a Figlet object
    fonts2 = []  # empty list wich will hold all the aviable fonts
    fonts2.extend(figlet.getFonts() ) # get all available fonts and add to the empty list

    if len(sys.argv) > 3 or len(sys.argv) == 2:  # check the number of arguments
        sys.exit("incorrect number of arguments")
    elif len(sys.argv) == 3:
        if (sys.argv[1] not in options or sys.argv[2] not in fonts2 ): # check if arguments are valid
            sys.exit("Incorrect arguments")

    s = input("Input: ")  # prompt the user
    if len(sys.argv) == 3:  # check the number of arguments
        figlet.setFont(font=sys.argv[2])  # set the comant line argument as a font
        print(  # print the output
            f"""Output:
             {figlet.renderText(s)}"""
        )
    else:  # if no arguments provided se random font
        figlet.setFont(font=random.choice(fonts2))
        print(  # print the output
            f"""Output:
                        {figlet.renderText(s)}"""
        )


main()  # call main
