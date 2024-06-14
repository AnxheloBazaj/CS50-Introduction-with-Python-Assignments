def main():
    expression = input('Expression:') # Prompt the user for an arithmetic expression
    x,y,z = expression.split(" ") # Splitting the  expression into three parts x, y, and z
    x = float(x) # Converting the value of x from string to a float
    z = float(z) # Converting the value of z from string to a float

    if y == '+': # Check the value of y to determine which mathematical operation to perform
        print(x + z )
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)

main() # call main

# Resources used : docs.python.org/3/library/stdtypes.html#string-methods
