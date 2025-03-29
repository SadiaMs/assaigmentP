AFFIRMATION = "I am capable of doing anything I put my mind to. ✨"

def main():
    print("\n🌟 Please type the following affirmation to remind yourself: 🌟\n")
    print(f"📝 {AFFIRMATION}\n")

    while True:
        user_input = input("👉 Type here: ")
        
        if user_input == AFFIRMATION:
            print("\n🎉 That's right! You are unstoppable! 🚀💪")
            break  # Exit loop if affirmation is correct
        else:
            print("\n❌ Hmmm... That wasn't quite right. Try again!\n")

if __name__ == "__main__":
    main()
