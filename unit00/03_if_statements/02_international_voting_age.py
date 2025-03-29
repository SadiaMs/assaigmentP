def can_vote(age: int, country: str, voting_age: int):
    """
    User ki age ko check karta hai aur batata hai ke user kisi specific country me vote de sakta hai ya nahi.
    """
    if age >= voting_age:
        print(f"You can vote in {country} where the voting age is {voting_age}.")
    else:
        print(f"You cannot vote in {country} where the voting age is {voting_age}.")

def main():
    # Voting age for each country
    VOTING_AGES = {
        "Pakistan": 18,
        "usa": 25,
        "uk": 48
    }

    # User input
    try:
        user_age = int(input("How old are you? "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Voting check for each country
    for country, age in VOTING_AGES.items():
        can_vote(user_age, country, age)

if __name__ == "__main__":
    main()
