# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.




def secondsInYear():
    user_input = input("Enter the number of year: ")
    days_per_year = 365
    hours_per_day = 24
    minutes_per_hour = 60
    seconds_per_minute = 60
    seconds_per_year = days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute * int(user_input)
    print("There are", seconds_per_year, "seconds in a year!")
secondsInYear()    