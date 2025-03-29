MINIMUM_HEIGHT: int = 50  # Minimum height requirement

def main():
    while True:
        height = input("How tall are you? (Press Enter to stop) ")
        
        if height == "":
            print("Exiting program. Have a great day!")
            break  # Stop the loop if the input is empty
        
        try:
            height = float(height)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride! 🎢")
            else:
                print("You're not tall enough to ride, but maybe next year! 😊")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == '__main__':
    main()
# The code checks if a person is tall enough to ride a roller coaster. If the height is less than the minimum requirement, it suggests that they might be able to ride next year.