



months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



def ask_year():
    year = input("Enter the year: ")
    try:
        val = int(year)

    except ValueError:
        print("Please enter the year as a number")
        year = input("Enter the year: ")

def ask_month():
    month = input("Enter the month: ")
    try:
        val2 = str(month)

    except ValueError:
        print("Please enter the month as text")
        month = input("Enter the month: ")


    if month not in months:
        print("Enter a correct month with the first letter capitalized. Check your spelling")
        ask_month()
    else:
        print("correct")
        #month = input("Enter the month: ")

def ask_day():
    day = input("Enter the day: ")
    try:
        val3 = int(day)

    except ValueError:
        print("Please enter the day as a number")
        day = input("Enter the day: ")

ask_year()
ask_month()
ask_day()