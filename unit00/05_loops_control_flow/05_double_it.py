def main():
    print("\n🚀 Welcome to the Doubling Challenge! 🔢\n")
    
    # User inputs the starting number
    curr_value = int(input("👉 Enter a number to start: "))
    
    print("\n📈 Doubling process begins:\n")

    while curr_value < 100:
        curr_value *= 2  # Double the number
        print(f"➡️ {curr_value}", end=" ")  # Display numbers in one line
    
    print("\n\n🎉 The value has reached or exceeded 100! Game Over. 🎯")

if __name__ == '__main__':
    main()
