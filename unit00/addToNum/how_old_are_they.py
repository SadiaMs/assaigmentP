def main():
    anton: int = 21  # Anton's age is given as 21 years old
    beth: int = 6 + anton  # Beth is 6 years older than Anton
    chen: int = 20 + beth  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is as old as Chen's age plus Anton's age
    ethan: int = chen  # Ethan is the same age as Chen

    # Print out all of the ages with emojis and styling! 🎉
    print("\n🎂 Age Information 🎂\n" + "=" * 20)
    print(f"🧑 Anton is {anton} years old")
    print(f"👩 Beth is {beth} years old")
    print(f"👨‍🦳 Chen is {chen} years old")
    print(f"🧑‍🦰 Drew is {drew} years old")
    print(f"👦 Ethan is {ethan} years old")
    print("=" * 20 + "\n🎉 That's all, folks! 🎉")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
