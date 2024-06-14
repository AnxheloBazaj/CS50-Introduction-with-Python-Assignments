def main(): #define main

    menu = {             # a dictionary which hold the item (key) and price(value)
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total =0 # variable which later on will hold the total value

    while True:  # infinite loop in order to continue prompting
        try: # a try statement which will try to exectue the following code
            item = input('Item: ',).title() # prompt the user for an item
            if item in menu: # check if item is in the menu(dict)
                 total+=menu[item] # update total by adding the value of the item with the current value
                 print(f"Total: ${total:.2f}") # print the total

        except EOFError: # handle the exception
                print() # move the user cursor on a new line
                break # break the loop
        except KeyError: # handle the exception
                pass # skip this error and do nothing
main() # call main
# resources used: https://docs.python.org/3/library/


