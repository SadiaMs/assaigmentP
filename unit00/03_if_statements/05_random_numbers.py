import random

N_NUMBERS = 10  # Number of random numbers to generate
MIN_VALUE = 1   # Minimum value in range
MAX_VALUE = 100 # Maximum value in range

def main():
    # Generate and print 10 random numbers in the range 1 to 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

if __name__ == '__main__':
    main()
