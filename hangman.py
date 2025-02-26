import random
import nltk
from nltk.corpus import words

WORD_LIST = words.words()

def choose_word(difficulty='medium'):
    if difficulty == 'easy':
        return random.choice([word for word in WORD_LIST if len(word) <= 5])
    elif difficulty == 'medium':
        return random.choice([word for word in WORD_LIST if 5 < len(word) <= 8])
    elif difficulty == 'hard':
        return random.choice([word for word in WORD_LIST if len(word) > 8])
    else:
        return random.choice(WORD_LIST)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        """
    ]
    return stages[incorrect_guesses]

def get_valid_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Please enter a single valid letter.")

def hangman():
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        word = choose_word(difficulty)
        guessed_letters = set()
        incorrect_guesses = 0
        max_incorrect_guesses = 6

        print("Welcome to Hangman!")
        print(display_hangman(incorrect_guesses))
        print(display_word(word, guessed_letters))

        while incorrect_guesses < max_incorrect_guesses:
            guess = get_valid_guess()

            if guess in guessed_letters:
                print("You already guessed that letter")
            elif guess in word:
                guessed_letters.add(guess)
                print("Correct")
            else:
                guessed_letters.add(guess)
                incorrect_guesses += 1
                print("Incorrect, you have {} guesses left".format(max_incorrect_guesses - incorrect_guesses))
            
            print(display_hangman(incorrect_guesses))
            print(display_word(word, guessed_letters))

            if all(letter in guessed_letters for letter in word):
                print("You win!")
                break

        else:
            print("You lose! The word was {}".format(word))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    hangman()