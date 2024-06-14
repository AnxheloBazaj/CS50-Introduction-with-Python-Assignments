def main():
    text = input('Input:') #prompt the user for text
    print(shorten(text))
def shorten(word):
    vowels = ['a','A','e','E','i','I','o','O','u','U'] # Create a list to hold the vowel uppercase and lowercase
    #vowels = ['a','e','i','o','u',]
    new_word=''  # variable which will store the new text without the vowels
    for char in word: # iterate over the users input
        if char not in vowels: # check if the character is not a vowel and add it to new_text
            new_word += char

    return new_word # return the new word
if __name__ == "__main__":
    main()
