def main():
    inputed_time = input('What time is it?') # Prompt the user for the time
    converted_time = convert(inputed_time)  # Convert the time
    if converted_time <= 7 or converted_time <=8: # Check whether the converted time corespond with any meal
        print('Breakfast time') # Print the coresponding meal based on the time
    elif converted_time <= 12 or converted_time <=13:
        print('Lunch time')
    elif converted_time <=18 or converted_time <=19:
        print('Dinner time')

def convert(time): # Create a function called convert
    hours, minutes = time.split(":") # Split time into hours and minutes
    hours = float(hours) # Converting the value of hours from string to a float
    minutes = float(minutes) # Converting the value of minutes from string to a float
    total_hours = (hours * 60 + minutes) / 60 # total number of hours


    return total_hours

if __name__ == "__main__": # Allows check50 to test your convert function separately.
    main() # Call main
