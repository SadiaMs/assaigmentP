def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # Cleaner and more Pythonic way!

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    print(in_range(n, low, high))  # Call function and print result

if __name__ == '__main__':
    main()
