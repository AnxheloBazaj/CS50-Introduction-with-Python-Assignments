def main():
    greeting = input('Greeting:').strip(' ').lower() # Prompt the user for the greeting
    if 'hello' in greeting: # Check if the greeting starts with hello and output $0 if yes
        print('$0')
    elif greeting.startswith('h'): # Check if the greeting starts with an “h” but not “hello”, output $20
        print('$20')
    else:                     # Otherwise output $100
        print('$100')

main() # Call main

# Resources used: docs.python.org/3/library/stdtypes.html#string-methods.
