def main():
    # Dictionary containing fruit names and their prices
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }

    total_cost = 0

    print("🍎 Welcome to the Fruit Shop! 🛒\n")
    
    for fruit, price in fruits.items():
        while True:
            try:
                quantity = input(f"How many ({fruit}) do you want?: ")
                
                if quantity.strip() == "":  # Allow user to press Enter to skip
                    quantity = 0
                else:
                    quantity = int(quantity)
                
                if quantity < 0:
                    print("❌ Please enter a valid non-negative number!")
                    continue
                
                total_cost += price * quantity
                break  # Exit the loop if input is valid
            
            except ValueError:
                print("⚠️ Invalid input! Please enter a whole number.")

    # Display total cost formatted to 2 decimal places
    print(f"\n🛍️ Your total is **${total_cost:.2f}** 💰")

if __name__ == '__main__':
    main()
