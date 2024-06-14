def main():
    #prompt the user for the answer
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    # remove spaces if any and return the string in lowercase if necessery
    answer2 = answer.strip(' ').lower()
    # check if answer is correct
    if answer2 == '42' or answer2 == 'forty-two' or answer2 == 'forty two':
        print('Yes') # print Yes if anser is correct
    else: # if answer is not correct print No
        print('No')

main() # call main
# resources used : Python library
