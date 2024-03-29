def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def find_anniversary(anniversary_date):
    anniversary_year = int(anniversary_date[-4:])
    if is_leap_year(anniversary_year):
        print("Given Anniversary Year:", anniversary_year, " (Leap Year)")
        print("Next Anniversary Date:", anniversary_date[:-4] + str(anniversary_year + 4))
    else:
        print("Given Anniversary Year:", anniversary_year, " (Non-Leap Year)")
        print("Previous Anniversary Date:", anniversary_date[:-4] + str(anniversary_year - 4))

anniversary_date = input("Enter Date (DD/MM/YYYY): ")
find_anniversary(anniversary_date)
