"""
Hangman Word Guessing Game (Console)
------------------------------------
- Downloads the English words list (cached locally as words.txt)
- Falls back to a built-in word list if offline
- 6 attempts, ASCII gallows art, duplicate guesses are not penalised
"""

import os
import random
import urllib.request

WORD_URL = (
    "https://raw.githubusercontent.com/first20hours/google-10000-english/"
    "master/google-10000-english-no-swears.txt"
)
WORD_FILE = "words.txt"
MAX_ATTEMPTS = 6

FALLBACK_WORDS = [
    "python", "variable", "function", "keyboard", "internet", "algorithm",
    "developer", "database", "computer", "network", "program", "software",
    "hangman", "machine", "learning", "browser", "terminal", "package",
]

STAGES = [
    # 0 wrong guesses
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    # 1
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    # 2
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    # 3
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    # 4
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    # 5
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    # 6 (game over)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def load_words():
    """Load words from local file, download if missing, else use fallback."""
    if not os.path.exists(WORD_FILE):
        try:
            print("Downloading word list...")
            urllib.request.urlretrieve(WORD_URL, WORD_FILE)
        except Exception:
            print("Could not download word list. Using built-in words.\n")
            return FALLBACK_WORDS

    try:
        with open(WORD_FILE, "r", encoding="utf-8") as f:
            words = [w.strip().lower() for w in f if w.strip()]
        # keep only alphabetic words of length 4+ for a decent game
        words = [w for w in words if w.isalpha() and len(w) >= 4]
        return words or FALLBACK_WORDS
    except OSError:
        return FALLBACK_WORDS


def display_word(secret, guessed):
    """Return masked word, e.g. 'p _ t h _ n'."""
    return " ".join(ch if ch in guessed else "_" for ch in secret)


def get_guess(guessed_letters):
    """Prompt until the user enters a single new, valid letter."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. No penalty - try another!")
        else:
            return guess


def show_status(secret, correct, wrong):
    print(STAGES[len(wrong)])
    print(f"\nWord:   {display_word(secret, correct)}")
    print(f"Wrong:  {' '.join(sorted(wrong)) if wrong else '-'}")
    print(f"Attempts left: {MAX_ATTEMPTS - len(wrong)}")


def victory_screen(secret):
    print("\n" + "=" * 40)
    print("   \U0001F389  CONGRATULATIONS! YOU WON!  \U0001F389")
    print(f"   The word was: {secret.upper()}")
    print("=" * 40)


def defeat_screen(secret):
    print(STAGES[MAX_ATTEMPTS])
    print("\n" + "=" * 40)
    print("        GAME OVER - YOU LOST")
    print(f"   The word was: {secret.upper()}")
    print("=" * 40)


def play(words):
    secret = random.choice(words)
    correct = set()
    wrong = set()

    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN")
    print(f"  Word has {len(secret)} letters. You have {MAX_ATTEMPTS} wrong guesses.")
    print("=" * 40)

    while len(wrong) < MAX_ATTEMPTS:
        show_status(secret, correct, wrong)

        # win check
        if all(ch in correct for ch in secret):
            victory_screen(secret)
            return

        guess = get_guess(correct | wrong)

        if guess in secret:
            correct.add(guess)
            print(f"\nGood job! '{guess}' is in the word.")
        else:
            wrong.add(guess)
            print(f"\nSorry, '{guess}' is not in the word.")

        # win check right after the guess
        if all(ch in correct for ch in secret):
            show_status(secret, correct, wrong)
            victory_screen(secret)
            return

    defeat_screen(secret)


def main():
    words = load_words()
    while True:
        play(words)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
