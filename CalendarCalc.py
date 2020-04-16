# File name: CalendarCalc.py
# Author name: Kali Hale
# Date: 9/29/2019
# Description: This will validate a date entered and, if the date is valid, tell the user how many days have passed
    # since the beginning of the year.

import math


def main():
    print("Enter a date and this calculator will tell you which day of the year your date is, eg. 2/29/2000 is the 60th "
          "day of the year")

    # get date
    global daynum
    datainput = input("Please enter your month, day, and four digit year in the format MM/DD/YYYY: ")
    print()
    month, day, year = datainput.split("/")
    month = int(month)
    day = int(day)
    year = int(year)

    # check year
    validyear = checkyear(int(year))

    leapyear = divyear(int(year))

    # check month
    validmonth = checkmonth(int(month))

    # check day
    validday = checkday(int(month), int(leapyear), int(day))

    if validyear == 0:
        print("Your year is out of range. Please try again.")
    if leapyear == 1:
        print("The year you have entered is a leapyear.")
    if validmonth == 0:
        print("Your month is incorrect. Please try again.")
    if validday == 0:
        print("Your day is not within the month. Please try again.")

    # calculate day
    if validyear == 1 and validmonth == 1 and validday == 1:
        if month <= 2:
            daynum = (31 * (month - 1)) + day
        elif month > 2 and leapyear == 1:
            daynum = ((31 * (month - 1) + day) - ((4 * month + 23) / 10)) + 1
        else:
            daynum = (31 * (month - 1) + day) - ((4 * month + 23) / 10)

    print("The date you entered:", month, "/", day, "/", year)
    if validyear == 1 and validmonth == 1 and validday == 1:
        print("is day", round(daynum), "of the year.")


def checkyear(y):
    validyear = 1
    if y > 3000:
        validyear = 0
    if y < 1000:
        validyear = 0
    return validyear


def divyear(y):
    leapyear = 1
    if math.remainder(y, 4) != 0:
        leapyear = 0
    if math.remainder(y, 100) == 0 and math.remainder(y, 400) != 0:
        leapyear = 0
    return leapyear


def checkmonth(m):
    validmonth = 1
    if m > 12:
        validmonth = 0
    if m < 1:
        validmonth = 0
    return validmonth


def checkday(m, leap, d):
    validday = 1
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 31:
            validday = 0
    elif m == 2 and leap == 1:
        if d > 29:
            validday = 0
    elif m == 2:
        if d > 28:
            validday = 0
    else:
        if d > 30:
            validday = 0
    return validday


main()
