def main():
    prompt = input("What's your favorite Animal Name? ")
    
    if prompt.isalpha():  # Checks if input contains only letters
        print(f"\n 🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩  \n\n\t🤠 Great! My favorite Animal is also 🌞 , {prompt}.\n\n 🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩\n\n")
    else:
        print("~~~  🚫  Please enter only alphabetic characters. 🫣  ~~~")

main()
