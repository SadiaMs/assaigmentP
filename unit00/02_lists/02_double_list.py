def main():
    print("🚀 Let's double each number in the list! 🔢✨")
    
    numbers: list[int] = [1, 2, 3, 4,5,6,7,8,9,10]  # Creates a list of numbers 🔢

    for i in range(len(numbers)):  # Loop through the indices of the list 🔄
        numbers[i] *= 2  # Double each element 🎯

    print(f"🎉 Doubled List: {numbers} 🎊")  # Print the updated list 🚀


# This provided line is required at the end of the Python file to call the main() function. 📌
if __name__ == '__main__':
    main()
