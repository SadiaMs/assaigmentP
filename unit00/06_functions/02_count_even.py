def count_even(lst):
    """
    Counts and prints the number of even numbers in the list.
    """
    count = sum(1 for num in lst if num % 2 == 0)  # Count evens using list comprehension
    print(f"🟢 Total even numbers: {count}")

def get_list_of_ints():
    """
    Reads integers from the user until they press enter and returns the list.
    """
    lst = []  
    while True:
        user_input = input("🔢 Enter an integer or press enter to stop: ")  
        if user_input == "":  # Stop if the user presses enter
            break
        try:
            lst.append(int(user_input))  # Convert input to an integer and add it to the list
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.")  

    return lst

def main():
    print("\n📢 Let's count even numbers in your list!\n")
    lst = get_list_of_ints()
    count_even(lst)
    print("\n✅ Done! Thanks for using the program. 🎉")

# Run the program
if __name__ == '__main__':
    main()
