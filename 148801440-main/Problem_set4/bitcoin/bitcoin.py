import requests # import request module
import json # import json module
import sys # import sys module

if len(sys.argv) == 2: # check the number of arguments
    try:
        bitcoinCount = float(sys.argv[1]) # initialize the second cmd line argm to a variable
    except ValueError: # handle the error
        sys.exit('Command-line argument is not a number') # if error exit the program

elif len(sys.argv) != 2: # check the number of arguments
    sys.exit('Missing command-line argument') # if incorrect number of argm exit program

try:
     #  Send a GET request to the CoinDesk API and store the server's response
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json") #  Send a GET request to the CoinDesk API and store the server's response
    api_response = response.json()
    # Convert the server's JSON response into a Python data structure and store it in api_response
    rate_USD = api_response["bpi"]["USD"]["rate_float"] # extract the bitcoin rate in USD and store it

    print(f"${rate_USD * bitcoinCount:,.4f}") # print the total value of bitcoins in USD

except requests.RequestException: # if exception encounterd exit the program
    sys.exit("Error Encounterd")
