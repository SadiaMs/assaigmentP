
import random


NUM_SIDES = 6  

def roll_dice():
    
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"🎲 {die1} + 🎲 {die2} = {total} 🎯")

def main():
    die1 = 10  
    print("\n🚀 Simulation Start!")
    print(f"🎲 die1 in main() starts as: {die1}\n")
    
  
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"\n🎲 die1 in main() ends as: {die1}")
    print("🏁 Simulation Ended!\n")


if __name__ == '__main__':
    main()