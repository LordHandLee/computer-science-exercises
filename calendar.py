



months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31,
          "September":30, "October":31, "November":30, "December":31}


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
        print(month)
        return str(month)
        #month = input("Enter the month: ")







#print(months.values())


ask_year()
#ask_month()
the_month = ask_month()

def check_days_in_month(day):
    print("checking")
    for mon in months:
        if the_month == mon:
            if int(day) > int(months[mon]):
                print("You have exceeded the number of days for this month.")
                return True
        else:
            return False

def ask_day():
    day = input("Enter the day: ")
    try:
        val3 = int(day)

    except ValueError:
        print("Please enter the day as a number")
        day = input("Enter the day: ")
    #check_days_in_month(day)
    if check_days_in_month(day) == True:
        ask_day()
    else:
        return

#print(the_month)
ask_day()