def double(num: int):
    """Returns the double of the given number."""
    return num * 2

def main():
    print("\n🚀 Let's double your number! 🔢")
    
    while True:
        try:
            num = int(input("✨ Enter a number: "))  
            break  # Exit loop if input is valid
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.")  
    
    result = double(num)
    print(f"🔁 Double that is: {result} 🎉")

# Run the program
if __name__ == '__main__':
    main()
