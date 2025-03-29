def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year or not.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    try:
        year = int(input("Please input a year: "))
        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == '__main__':
    main()
# The code checks if a year is a leap year. A year is a leap year if: