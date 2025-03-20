def main():
    try:
        num1 = input("Enter 1st Number: ")
        num1 = int(num1)
        num2 = input("Enter 2nd Number: ")
        num2 = int(num2)
    
        add = num1 + num2
        print(f"{num1} + {num2} = ⭐ {add} ✔️")
    except ValueError:
        print("\n✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ \n\n \t Please enter only numbers 😱 \n \n✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️")


main()
