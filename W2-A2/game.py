import random
import string

class GameProcess:

    #generates random word to guess from a list of words
    def get_random_word():

        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        return random.choice(words)

    #creates a list of blanks for the word to guess
    def make_blanks(word):

        return ["_" for _ in word]


    #prompts user to enter a letter and checks if it is valid
    def prompt_for_letter(used_letters):

        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in used_letters:
                print(" → You already tried that letter.")
                continue
            return guess


    #reveals the guessed letter in the blanks if it is present in the word
    def reveal_letters(word, blanks, letter):

        found_any = False
        for i, ch in enumerate(word):
            if ch == letter and blanks[i] == "_":
                blanks[i] = letter
                found_any = True
        return found_any


    #checks if all blanks have been filled
    def all_blanks_filled(blanks):

        return "_" not in blanks


#plays the word guessing game
class WordGame:
    def play_game(self, max_lives=6):

        secret = GameProcess.get_random_word()
        blanks = GameProcess.make_blanks(secret)
        lives = max_lives
        used = set()

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(secret)} letters.")
        print(" ".join(blanks))

        while True:
            # Ask the user to guess a letter
            guess = GameProcess.prompt_for_letter(used)
            used.add(guess)

            # Is the guessed letter in the word?
            if GameProcess.reveal_letters(secret, blanks, guess):
                print("\n Well done, Nice job! You found a letter.")
                print(" ".join(blanks))
                # Are all blanks filled?
                if GameProcess.all_blanks_filled(blanks):
                    print("\n Congratulation! You guessed the word!")
                    print(f"Word: {secret}")
                    print("GAME OVER")
                    break
            else:
                # Lose a life
                lives -= 1
                print(f"\nNope. You lose a life. Lives left: {lives}")
                print(" ".join(blanks))

                # Have they run out of lives?
                if lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {secret}")
                    print("GAME OVER")
                    break

            # (loop continues to ask for another letter)
