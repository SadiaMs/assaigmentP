def main():
    while True:  # Keep asking until valid input is given
        try:
            fahrenheit = int(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            print(f"\n{fahrenheit}°F = {celsius:.2f}°C")  # Rounded to 2 decimal places
            break  # Exit the loop if input is valid
        except ValueError:
            print("\n✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ \n\n \t Please enter only numbers 😱 \n \n✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️ ✖️")

main()
