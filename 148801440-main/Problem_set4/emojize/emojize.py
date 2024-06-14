import emoji  # import emoji library


def main():  # define main
    emojize = input("Input: ")  # prompt the user for input and store it in a variable

    # convert any emoji names in the user's input into their corresponding emoji symbols and print them
    print(emoji.emojize(emojize, language="alias"))


main()  # call main
