import random

def main():
    print("🏏 Welcome to the Cricket Guessing Game! 🏏")
    print("You have 6 balls to score as many runs as possible!\n")

    total_score = 0
    balls = 6

    for ball in range(1, balls + 1):
        secret_number = random.randint(1, 6)  # Har ball par ek new random number
        print(f"Ball {ball}: It's your turn!")

        try:
            guess = int(input(f"Enter a number between 1 and 6: "))

            if guess < 1 or guess > 6:
                print("❌ Invalid input! Please enter a number between 1 and 6.")
                continue  # Galat input pe wapas se wahi ball repeat hogi

            if guess == secret_number:
                print("🏏 Six! Well played! 🎉")
                total_score += 6  # Sahi guess par 6 runs milenge
            else:
                print(f"❌ Missed! The correct number was: {secret_number}")
        
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    print(f"\n🏆 Game Over! Your total score: {total_score} runs 🏆")

if __name__ == '__main__':
    main()
