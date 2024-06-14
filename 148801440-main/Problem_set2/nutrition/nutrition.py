def main():
    item = input('Item: ').lower() # prompt the user and convert to lowercase
    fruits = {      # dictionary for the fruits and coresponding calories
        'apple':'130', 'avocado': '50', 'banana': '110',
        'cantaloupe': '50', 'grapefruit': '60', 'grapes': '90',
        'honeydew melon': '50', 'kiwifruit': '90', 'lemon': '15',
        'lime': '20', 'nectarine': '60', 'orange': '80',
        'peach': '60', 'pear': '100', 'pineapple': '50',
        'plums': '70', 'strawberries': '50', 'sweet cherries': '100',
        'tangerine': '50', 'watermelon': '80'
    }

    for fruit in fruits:  # iterate over the values of the dictionary
        if item == fruit: # check if the users input equals with value of fruit
            print(f'Calories: {fruits[item]}') # output the calories of the matching fruit

main() #call main
