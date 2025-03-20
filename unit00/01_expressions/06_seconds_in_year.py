"""
📅 Seconds in a Year Calculator ⏳
---------------------------------
This program calculates the number of seconds in a year
using constants and displays the result in a clear format. 🧮
"""

# 🕰️ Constants for time conversion
DAYS_PER_YEAR: int = 365     # 🌍 Days in a year
HOURS_PER_DAY: int = 24      # ⏳ Hours in a day
MIN_PER_HOUR: int = 60       # ⏰ Minutes in an hour
SEC_PER_MIN: int = 60        # ⌛ Seconds in a minute

def main():
    # 🧮 Calculate total seconds in a year
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # 🎯 Display the result using an f-string for better formatting
    print(f"🌟 There are {seconds_in_year:,} seconds in a year! ⏳🎉")

# 🔥 Standard Python practice to execute main function
if __name__ == '__main__':
    main()
