def is_leap_year() -> bool:
    year = int(input("Enter a year: "))
    if (year % 4 == 0) and (year % 400 == 0 and year % 100 == 0):
        print(f"El año {year} es bisiesto")
        return True
    else:
        print(f"El año {year} no es bisiesto")
        return False

print(is_leap_year())
