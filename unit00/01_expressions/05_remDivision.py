"""
➗ Division Calculator ➗
--------------------------------------
This program asks the user for two numbers 
and calculates:
1️⃣ The quotient (integer division)
2️⃣ The remainder of the division (modulo)
"""

def main():
    print("\n➗ Division & Remainder Calculator ➗\n")

    try:
        # Get the numbers from the user
        dividend: int = int(input("🔢 Please enter an integer to be divided: "))
        divisor: int = int(input("🔢 Please enter an integer to divide by: "))

        # Check if the divisor is zero to prevent division by zero error
        if divisor == 0:
            print("\n❌ Error: Division by zero is not allowed! ❌")
            return
        
        # Perform integer division and find remainder
        quotient: int = dividend // divisor  # Integer division
        remainder: int = dividend % divisor  # Remainder

        # Display the result with formatted output
        print(f"\n✅ The result of {dividend} ÷ {divisor} is {quotient} with a remainder of {remainder}.✔️")

    except ValueError:
        # Handle invalid inputs (non-numeric values)
        print("\n❌ Please enter valid integers only! ❌")

# Standard Python practice to ensure the script runs correctly
if __name__ == '__main__':
    main()
