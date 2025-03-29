def get_user_numbers():
    """
    Collects numbers from the user until they enter a blank line.
    Returns a list of entered numbers.
    """
    user_numbers = []
    
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")
        
        if user_input == "":
            break  # Stop taking input when the user enters nothing
        
        try:
            num = int(user_input)  # Convert input to integer
            user_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Counts occurrences of each number in the list and stores them in a dictionary.
    """
    num_dict = {}

    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Efficient way to update count
    
    return num_dict

def print_counts(num_dict):
    """
    Prints each unique number and how many times it appears.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Main function to execute the steps.
    """
    user_numbers = get_user_numbers()
    
    if not user_numbers:
        print("No numbers were entered.")
        return
    
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
