def print_divisors(num: int):
    """Prints all divisors of num (numbers that divide num without remainder)."""
    print(f"Here are the divisors of {num}: ", end="")  # Print header without newline
    for i in range(1, num + 1):  # Start from 1 up to num (inclusive)
        if num % i == 0:
            print(i, end=" ")  # Print divisors on the same line
    print()  # Move to the next line after printing all divisors

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
