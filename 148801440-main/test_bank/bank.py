def main():
    greet = input('Greeting:').strip(' ')#.lower() # Prompt the user for the greeting

    print(value(greet))
def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting.startswith('hello'):# Check if the greeting starts with hello and output $0 if yes
        return '$0'
    elif greeting.startswith('h'): # Check if the greeting starts with an “h” but not “hello”, output $20
        return '$20'
    else:                     # Otherwise output $100
        return '$100'

if __name__ == "__main__":
    main()

# Resources used: docs.python.org/3/library/stdtypes.html#string-methods.
