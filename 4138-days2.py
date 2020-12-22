def isYearLeap(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year):
        dayList[1] = 29
    return dayList[month-1]

def dayOfYear(year, month, day):
    if day <= daysInMonth(year, month):
        return True

print(dayOfYear(2000, 12, 31))