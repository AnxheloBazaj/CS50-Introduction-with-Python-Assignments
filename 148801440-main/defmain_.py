def main():  # define main
    # !!!!! Please enter the date in one of the following formats: "September 8, 1234" or "9/8/1234"
    months = {  # dictionary which holds months as keys and numbers as their representing value
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    mm = None  # empty variable wihout a type which will hold the month
    dd = None  # empty variable wihout a type which will hold the day
    yyyy = None  # empty variable wihout a type which will hold the year

    while True:  # infinite loop to keep prompting the user
        try:  # try statement which will try the following code
            date = input("Date: ")  # prompt the user for input (date)

            if "/" in date:  # check if the input contains a slash(/)
                mm, dd, yyyy = map(
                    int, date.split("/")
                )  # Splitting the date at the slash into three parts mm, dd, and yyyy amd converting them to int

                if mm <= 12 and dd <= 31:
                    break  # check if the month and day are within limits and break out of the loop

            if "," in date:  # check if the input contains a comma
                mm, dd, yyyy = date.split(" ")  # Splitting the date at the whitespaces
                dd = dd.strip(",")  # remove the comma wich was left from the split
                dd = int(dd)  # convert dd (day) to int
                yyyy = int(yyyy)  # convert yyyy(year) to int
                if mm in months:  # check if the month is in the month dictionary
                    mm = months[
                        mm
                    ]  # asign the value of the month key to month variable
                    mm = int(mm)  # convert the value to int
                    if dd <= 31 and mm <= 12:
                        break  # check if the days and months are within limits then break out of the loop

        except ValueError:
            pass  # handle the error

    print(f"{yyyy}-{mm:02}-{dd:02}")  # print the year, month and day


main()  # call main
# Resources used : https://cs50.ai/chat
#                  https://docs.python.org/3/library/
