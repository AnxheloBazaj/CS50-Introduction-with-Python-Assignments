def main():
    m = int(input('m:')) # ask user for mass and convert to int
    c = pow(300000000, 2) # the value of the speed of light square
    E = m * c      #  energy using the formula E = m*c^2
    print(f"E:{E}") # print the energy

main() #call main

# Resources used : docs.python.org/3/library/functions.html#input.
#                  docs.python.org/3/library/functions.html#int.
#                  docs.python.org/3/library/functions.html.
