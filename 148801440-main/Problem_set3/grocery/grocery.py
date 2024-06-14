def main(): # define main
   fruits = {} # empty dictionary which will get keys and values later on
   while True: # infinite loop to continuously prompt the user
        try: # try statement
            item = input().upper() # prompt the user
            if item == '': # check if the useres enters only white spaces and ignore them
                pass
            elif item not in fruits: # if the key is not on the dict add it
                fruits[item] = 1 # add the key to the dict
            else:
                fruits[item] = fruits[item] +1 # if the key is already in the dict raise its value by 1

        except EOFError: #  handle the exception
            for keys in sorted(fruits): # iterate over the sorted dict
                print( fruits[keys], keys) # print the value and the key
            break # break out of the loop
        except: # handle any other potential errors and ignore them
            pass

main() #call main
# resources used : https://cs50.ai/chat ...helped me discover sorted() and explained it to me
#                  https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#                  https://docs.python.org/3/library/
