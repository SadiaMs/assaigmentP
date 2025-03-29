def make_sentence(word: str, part_of_speech: int):
    """Prints a sentence using the given word based on its part of speech."""
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid choice! Part of speech must be 0, 1, or 2.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
