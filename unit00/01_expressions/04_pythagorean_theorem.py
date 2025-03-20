"""
📐 Pythagorean Theorem Calculator 📐
--------------------------------------
This program calculates the length of the hypotenuse (BC) 
of a right triangle using the Pythagorean theorem:

BC² = AB² + AC²
"""

# Import the math module for square root function
import math  

def main():
    print("\n🔺 Right Triangle Hypotenuse Calculator 🔺\n")

    try:
        # Take user input for two perpendicular sides
        ab: float = float(input("📏 Enter the length of AB: "))
        ac: float = float(input("📏 Enter the length of AC: "))

        # Apply the Pythagorean theorem: BC = sqrt(AB² + AC²)
        bc: float = math.sqrt(ab**2 + ac**2)

        # Display the result with formatted output
        print(f"\n✅ The length of BC (the hypotenuse) is: {bc:.2f} ✔️ ")
    
    except ValueError:
        # Handle invalid inputs (non-numeric values)
        print("\n❌ Please enter valid numerical values! ❌")

# Standard Python practice to ensure the script runs correctly
if __name__ == '__main__':
    main()
