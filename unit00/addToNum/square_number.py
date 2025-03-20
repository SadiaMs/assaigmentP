def main():
    print("\n🟨 Welcome to the Square Calculator! 🔢\n")

    try: 
        #user se number lene k liye
        num = float(input("💡 Type a number to see its square: ➡️    "))

        # مربع کا حساب
        square = num ** 2

        #print the result
        print(f"\n✅ {num} squared is {square} ✔️")

    except ValueError:
        print("\n❌ Please enter a valid number! 🔢")


if __name__ == '__main__':
    main()
