def is_leap_year(int: year) -> bool:
    if (year % 4 == 0) and (year % 400 == 0 and year % 100 == 0):
        return True
    else:
        return False
