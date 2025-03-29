def read_phone_numbers():
    """
    Collects names and phone numbers from the user to store in a dictionary.
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Enter name (or press Enter to stop): ")
        if name == "":
            break  # Stop taking input when the user presses Enter
        
        number = input(f"Enter number for {name}: ")
        
        if name in phonebook:
            print(f"Updating existing contact for {name}.")
        
        phonebook[name] = number  # Store name-number pair

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all contacts in the phonebook.
    """
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\n📞 Phonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """
    Allows the user to look up numbers by name.
    """
    while True:
        name = input("\nEnter name to look up (or press Enter to stop): ")
        if name == "":
            break
        
        if name in phonebook:
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")

def main():
    """
    Runs the phonebook application.
    """
    print("📖 Welcome to the Phonebook!")
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
