#Excercise5_Calendar
#Calendar
def days_in_month(): #defines function called days_in_month
    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    month = int(input("Enter the month (1-12): ")) #line of code that will be used to get user input
    year = int(input("Enter the year: "))
    
    if month < 1 or month > 12:
        print("Invalid month, Please enter a number between 1 and 12.") #Code will get the number of the month
        return

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
            print(f"February has 29 days in {year}.")
        else:
            print(f"February has {month_days[month]} days in {year}.") #Will check if it is a leap year
    else:
        print(f"The month {month} has {month_days[month]} days.") #Gets days for other months

if __name__ == "__main__":
    days_in_month() #Calls back function


    



