"""Terminal Hangman game. Run: python hangman.py"""
import random

WORDS = ["PYTHON", "NETWORK", "COMPUTER", "HANGMAN", "PROGRAM", "KEYBOARD", "CLOUD", "SOFTWARE"]

STAGES = [
r"""
 +---+
 |   |
     |
     |
     |
     |
=========""",
r"""
 +---+
 |   |
 O   |
     |
     |
     |
=========""",
r"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========""",
r"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========""",
r"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========""",
r"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========""",
r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========""",
]

def play_game():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    max_mistakes = 6

    print("\n=== HANGMAN ===")
    while True:
        print(STAGES[len(wrong)])
        masked = " ".join(letter if letter in guessed else "_" for letter in word)
        print("\nWord:", masked)
        print("Guessed letters:", " ".join(sorted(guessed | wrong)) or "None")
        print(f"Mistakes left: {max_mistakes - len(wrong)}")

        if all(letter in guessed for letter in word):
            print("\nYou win! The word was:", word)
            return
        if len(wrong) >= max_mistakes:
            print(STAGES[6])
            print("\nGame over! The word was:", word)
            return

        guess = input("Guess one letter (or type quit): ").strip().upper()
        if guess == "QUIT":
            print("Game ended. The word was:", word)
            return
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter A-Z.")
            continue
        if guess in guessed or guess in wrong:
            print("You already guessed that letter. No penalty.")
            continue
        if guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            wrong.add(guess)
            print("Incorrect.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
