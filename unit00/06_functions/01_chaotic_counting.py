import random

# Probability of stopping early
DONE_LIKELIHOOD = 0.3  

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            print("😵 I feel like stopping now...")
            return  # Ends the function early
        print(f"🔢 {curr_num}")  # Prints number with emoji

def main():
    print("\n🚀 I'm going to count until 10 or until I feel like stopping, whichever comes first...\n")
    chaotic_counting()
    print("\n✅ I'm done!")

# Run the program
if __name__ == "__main__":
    main()
