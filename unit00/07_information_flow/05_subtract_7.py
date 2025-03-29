def subtract_seven(num: int) -> int:
    """
    🎯 Subtracts 7 from the given number and returns the result.
    """
    return num - 7


def main():
    print("🔥 Let's do some quick math! 🔢")
    
    num: int = 7
    result = subtract_seven(num)
    
    print("\n✅ Original Number: ", num)
    print("➖ Subtracting 7...")
    print("🎯 Final Result: ", result, "🎉 (Should be zero!)")


# 🚀 Execute the program
if __name__ == '__main__':
    main()
