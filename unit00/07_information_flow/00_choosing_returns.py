ADULT_AGE: int = 18  # U.S. legal adult age

def is_adult(age: int) -> bool:
    """Returns True if age is 18 or older, otherwise False."""
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()
