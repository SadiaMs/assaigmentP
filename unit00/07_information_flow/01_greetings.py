def greet(name: str):
    """Prints a greeting message with the given name."""
    print("Greetings", name + "!")

def main():
    name = input("What's your name? ")
    greet(name)  # Call greet function to print the greeting

if __name__ == '__main__':
    main()
