def is_odd(value: int):
    """Checks if a value is odd. Returns True if odd, False if even."""
    return value % 2 == 1  # Returns True for odd numbers, False for even

def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

if __name__ == '__main__':
    main()
