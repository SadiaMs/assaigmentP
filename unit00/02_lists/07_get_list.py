def get_user_list():
    """
    Continuously prompts the user to enter values to be stored in a list.
    Stops when the user presses enter without typing anything.
    
    Returns:
        list: The final list of entered values.
    """
    print("\n🔹 Enter values one by one. Press 'Enter' without typing anything to stop.")

    lst = []
    while True:
        val = input("➤ Enter a value: ").strip()
        if not val:  # Stop when input is empty
            break
        lst.append(val)

    return lst

def main():
    """
    Main function to handle user input and display the final list.
    """
    user_list = get_user_list()
    
    print("\n✅ Here's the list:", user_list if user_list else "⚠️ No values were entered.")

if __name__ == '__main__':
    main()
