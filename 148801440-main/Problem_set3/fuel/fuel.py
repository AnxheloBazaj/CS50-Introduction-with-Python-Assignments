def main(): # define main
    capacity= fuel_gauge() # variable which will hold the returned value from fuel_gauge function
    print(capacity) # print the value of capacity variable

def fuel_gauge(): # define fuel_gauge function

    while True: # while loop which is needed to run for as long as we dont break from it

        try: # try statement which will try to execute the following code

            get_fraction = input('Fraction: ') #promt the user for input(fraction)
            x, y = get_fraction.split('/') # split the input into two new variables
            x =int(x) # convert the values from string to integer
            y = int(y)# convert the values from string to integer
            percentage = (100//y) * x # a fomula to calculate percentage

            if y <=100 and y >= x or y==x: # check if the value of y is than or equal to 100 and if y is bigger or equal to x
                if percentage >= 99: return 'F' # if percentage is bigger than or equal to 99 return F(short for full)
                elif percentage<= 1: return 'E' # if percentage is less than or equal to 99 return E(short for empty)
                return f'{percentage}%' # return the percentage (if any of the conditions is met the return statement will break out of the loop)


        except (ValueError, ZeroDivisionError): # exception for any potential errors
            pass


main() #call main
#resources used : https://docs.python.org/3/reference/compound_stmts.html#
# i had a bit of a problem with check number 4, instead of 67 my code returns 66 and i couldnt find a way to fix it ...thank you:)
