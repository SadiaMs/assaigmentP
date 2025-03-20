def main():
    print("\n🔺 Welcome to the Triangle Perimeter Calculator! 🔺\n")

    try:
       
        side1 = float(input("📏 What is the length of side 1? ➡️   "))
        side2 = float(input("📏 What is the length of side 2? ➡️   "))
        side3 = float(input("📏 What is the length of side 3? ➡️   "))

        # پیریمیٹر کا حساب
        perimeter = side1 + side2 + side3

        
        print("\n✅ The perimeter of the triangle is: " + str(perimeter) + " units ✔️  ")

    except ValueError:
        print("\n❌ Please enter a valid number! 🔢  ")

if __name__ == '__main__':
    main()
