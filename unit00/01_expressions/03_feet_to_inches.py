"""
📏 Feet to Inches Converter 📏
-----------------------------------
This program converts a given length in feet to inches.
1 foot = 12 inches
"""

# Define a constant for conversion
INCHES_IN_FOOT: int = 12  

def main():
    print("\n📌 Feet to Inches Converter 📌\n")

    try:
        # Take user input for the number of feet
        feet: float = float(input("🔢 Enter the number of feet: "))

        # Convert feet to inches
        inches: float = feet * INCHES_IN_FOOT  

        # Display the result
        print(f"\n✅ {feet} feet is equal to {inches} inches! 📏")
    
    except ValueError:
        # Handle invalid inputs (non-numeric values)
        print("\n❌ Please enter a valid number! ❌")

# Standard Python practice to ensure the script runs correctly
if __name__ == '__main__':
    main()
