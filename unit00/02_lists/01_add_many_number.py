def add_many_numbers(numbers: list[int]) -> int:
    """
    🔢 Takes in a list of numbers and returns the sum of those numbers. 🧮✨
    """
    return sum(numbers)  # Using Python's built-in sum function 🏆


# No need to edit code beyond this point 🚀

def main():
    print("🎯 Let's add some numbers together! 🤓")
    
    numbers: list[int] = [1, 2, 3, 4, 5,6,7,8,9,10]  # Make a list of numbers 🔢
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list ✨
    
    print(f"📝 The sum of {numbers} is: 🎉 {sum_of_numbers} 🎊")  # Print out the sum 🏆
    

if __name__ == '__main__':
    main()
