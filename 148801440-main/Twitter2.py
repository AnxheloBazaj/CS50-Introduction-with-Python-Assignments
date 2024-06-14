def main():
    text = input('Input:') #prompt the user for text
    vowels = ['a','A','e','E','i','I','o','O','u','U'] # Create a list to hold the vowel uppercase and lowercase
    new_text=''  # variable which will store the new text without the vowels
    for char in text: # iterate over the users input
        if char not in vowels: # check if the character is not a vowel and add it to new_text
            new_text += char

    print('Output:',new_text) # Print the new text

main()# call main
