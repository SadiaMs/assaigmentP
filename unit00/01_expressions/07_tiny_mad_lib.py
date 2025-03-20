import time
import random

# 🎭 Motivational Messages
motivational_quotes = [
    "🌟 Your mind is like a parachute—it works best when open!",
    "🚀 Mistakes are proof that you are trying. Keep going!",
    "🎭 Laughter is the best therapy, and it's free!",
    "💡 You are braver than you believe, stronger than you seem, and smarter than you think!",
    "🎉 Life is 10% what happens to you and 90% how you react to it. So react like a boss!"
]

# 🤣 Funny Endings
funny_endings = [
    "😂 And that's how {} accidentally became a fortune teller on TikTok!",
    "😱 Suddenly, a talking parrot appeared and said, 'Trust the universe!' 🦜",
    "🤣 Turns out {} was reading last year's horoscope... Oops!",
    "🚀 {} then started a YouTube channel called 'Astro Vibes & Fries'. 🍟",
    "🤔 And that's when {} realized... horoscopes are just really poetic guesses! 😆",
    "🛸 An alien landed and asked {} for advice on intergalactic astrology. 👽"
]

# 🔮 Horoscope Predictions
horoscopes = {
    "Aries": "🔥 Your energy is unstoppable today! Take risks but avoid running with scissors.",
    "Taurus": "🌿 A peaceful day ahead. Unless you step on a Lego. Then, not so peaceful.",
    "Gemini": "🗣️ Communication is key! But if no one listens, try speaking in pirate slang. 🏴‍☠️",
    "Cancer": "💖 Emotions are strong today. Perfect time to cry over a puppy video.",
    "Leo": "🌞 You are shining bright! Just don’t blind your friends with your awesomeness.",
    "Virgo": "📋 Organization is your superpower today! Use it wisely, like alphabetizing your snacks.",
    "Libra": "⚖️ Balance is important. Try balancing a spoon on your nose for extra luck.",
    "Scorpio": "🕵️‍♂️ A mystery unfolds! Like where all your socks disappear in the laundry.",
    "Sagittarius": "🏹 Adventure calls! Or maybe it's just your phone ringing. Either way, answer it!",
    "Capricorn": "🏆 Hard work pays off. But first, coffee. Or maybe a donut. Then work.",
    "Aquarius": "🌊 A wave of creativity is coming! Just don’t drown in it.",
    "Pisces": "🎭 Dream big! But also set an alarm, or you’ll be dreaming all day."
}

def main():
    print("🔮 Welcome to the Hilarious Horoscope Mad Libs Game! 🎭")
    time.sleep(1)

    # 📝 User Inputs
    name = input("💬 Enter your name: ")
    age = input("📅 Enter your age: ")
    zodiac_sign = input("♈ Enter your Zodiac sign: ")
    emotion = input("😊 How are you feeling today? (e.g., happy, excited, confused): ")
    activity = input("🎨 What's one thing you love doing? (e.g., dancing, binge-watching): ")
    object1 = input("🕰️ Name a random object near you: ")
    weird_food = input("🍔 Name a weird food you’d try (e.g., pickle-flavored ice cream): ")

    print("\n✨ Consulting the stars...")
    time.sleep(2)

    # 📜 Horoscope & Motivational Ending
    horoscope_message = horoscopes.get(zodiac_sign, "The stars are too busy watching Netflix to answer. 😆")
    funny_ending = random.choice(funny_endings).format(name)
    motivational_message = random.choice(motivational_quotes)

    # 📖 Horoscope Story
    story = f"""
    🎭 **Assalam o Alaikum1  {name}! Your Horoscope for today:**  

    🔮 **{zodiac_sign} - {horoscope_message}**  

    🌟 You woke up feeling **{emotion}**. To relax, you spent time **{activity}**.  
    While doing so, you found an old **{object1}** and decided to use it as a hat. 🎩  
    Then, out of nowhere, a waiter appeared and offered you **{weird_food}**.  
    You took a bite... and your life was never the same.  

    {funny_ending}  

    ✨ **Motivational Thought:** {motivational_message}  
    """

    print("\n🌟 Your Hilarious Horoscope Story:")
    print(story)

    print("\n👩‍🎓 Sadia 370350 - Student at GIAIC Khi 🎭")

if __name__ == "__main__":
    main()
