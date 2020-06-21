#19
days_of_the_week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
month_dict = {"January": 31, "February": 28, "March" : 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}
leap_month_dict = {"January": 31, "February": 29, "March" : 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31}

year = 1900
date = 1
while True:
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        days = 0
        for mounth in leap_month_dict:
            days += leap_month_dict[mounth]
        print(year, end=":")
        print(days)
    else:
        days = 0
        for mounth in month_dict:
            days += month_dict[mounth]
        print(year, end=":")
        print(days)
    if year == 2000:
        break
    year += 1

