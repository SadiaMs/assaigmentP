def num_in_stock(fruit: str) -> int:
    """
    This function returns the number of fruit Sophia has in stock. 🍏🍌🍍
    """
    inventory = {
        "apple": 2,
        "durian": 4,
        "pear": 1000
    }
    
    return inventory.get(fruit, 0)  # Return 0 if the fruit is not in stock


def main():
    fruit = input("🍓 Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock > 0:
        print("✅ This fruit is in stock! Here is how many: 🍉🍎🍊")
        print(f"📦 {stock} available!")
    else:
        print("❌ This fruit is not in stock. 😔")


if __name__ == '__main__':
    main()
