MAX_LENGTH: int = 3

def shorten(lst):
    """
    List ko chhota karta hai agar uska size MAX_LENGTH se zyada ho.
    Jo elements remove honge, unko print karega.
    """
    print("\nRemoving extra elements...")
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

    print("\nFinal List:", lst)

def get_lst():
    """
    User se ek list input lene ka function.
    Jab user khaali enter press karega, list input lena band ho jayega.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list (press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)
    
    print("\nOriginal List:", lst)
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
