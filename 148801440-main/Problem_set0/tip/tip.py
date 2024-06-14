def main():
    dollars = dollars_to_float(
        input("How much was the meal? ")
    )  # prompt the user for the ammount and convert to float
    # prompt the user for the percentage tip and convert it to float
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (
        dollars * percent
    )  # calculate the tip by multiplying the ammount with the percentage of the tip
    print(f"Leave ${tip:.2f}")  # print the tip ammount


def dollars_to_float(d):  # define a function called dollars_to_float
    d = float(
        d.strip("$")
    )  # remove the dollar sing from the input and convert to float
    return d


def percent_to_float(p):  # define a function called percent_to_float
    p = (
        float(p.strip("%")) / 100
    )  # remove the percentage sing from the input, convert to float and divide by 100
    return p


main()  # call main function
