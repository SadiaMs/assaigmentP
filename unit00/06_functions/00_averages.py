def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b
    """
    return (a + b) / 2  # Calculate the average

def main():
    print("\n📏 Let's Find the Average Between Two Numbers! 🤓\n")

    # User inputs two numbers
    num1 = float(input("🔢 Enter the first number: "))
    num2 = float(input("🔢 Enter the second number: "))

    # Calculate and display the average
    avg = average(num1, num2)
    print(f"\n📊 The average of {num1} and {num2} is: 🎯 {avg:.2f}")

    print("\n✅ Thank you for using the Average Finder! 🚀")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
