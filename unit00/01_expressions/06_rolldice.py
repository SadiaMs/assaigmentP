"""
🎲 Dice Rolling Simulator 🎲
--------------------------------------
This program simulates rolling two dice, 
displays their individual results, and 
calculates the total sum.
"""

import random  # Import the random module to simulate dice rolls

# Constant for the number of sides on each die
NUM_SIDES: int = 6  

def main():
    print("\n🎲 Welcome to the Dice Rolling Simulator! 🎲\n")

    # Rolling two dice
    die1: int = random.randint(1, NUM_SIDES)  # Random number between 1 and 6
    die2: int = random.randint(1, NUM_SIDES)  # Random number between 1 and 6
    
    # Calculating total
    total: int = die1 + die2  

    # Display results
    print(f"🎲 Dice have {NUM_SIDES} sides each.")
    print(f"🎲 First die rolled: {die1}")
    print(f"🎲 Second die rolled: {die2}")
    print(f"✨ Total of two dice: {total} ✨\n")

# Standard Python practice to run the main function
if __name__ == '__main__':
    main()
