def main():
    amount_due = 50 # variable which holds the amount due
    valid_coins = [25, 10, 5] # list eith all the valid coins
    inserted_amount = 0 # variable which the total amount inserted

    while inserted_amount < 50: # loop which will run for as long the condition is true
        print(f'Amount Due: {amount_due}') # output the amount due
        coin = int(input('Insert Coin: ')) # prompt the user for input(coins) and convert to int
        if coin not in valid_coins: # if the coin inserted is not on the list continue to prompt the user
            continue
        elif coin in valid_coins  :  # if the coin inserted is on the list then substract the amount due with
            amount_due -= coin       # the coin
            inserted_amount += coin  # add the coin to the inserted amount
            if amount_due == 0 :     # if the amount due is equal to zero break out of the loop
                break
            else:                    # if the amount due is not equal to zero then continue
                continue

    print('Change Owed:', inserted_amount-50) # output the remaining change if any by substracting the inserted amount with 50

main() # call main

