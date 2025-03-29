from typing import List

def get_first_element(lst: List[str]) -> None:
    """
    Prints the first element of a provided non-empty list.
    """
    print(f"\n🟢 The first element in the list is: {lst[0]}")

def get_lst() -> List[str]:
    """
    Prompts the user to enter elements one by one to form a list.
    Returns:
        List[str]: The user's list input.
    """
    print("\n🔹 Enter elements for the list. Press 'Enter' without typing anything to finish.")
    
    lst = []
    while True:
        elem = input("➤ Enter an element: ").strip()
        if not elem:
            break
        lst.append(elem)

    return lst

def main() -> None:
    """
    Main function to get the user list and print its first element.
    """
    user_list = get_lst()
    
    if user_list:  # Just in case, though it's guaranteed to be non-empty.
        get_first_element(user_list)
    else:
        print("\n⚠️ No elements were entered. Please restart and enter at least one item.")

if __name__ == "__main__":
    main()
