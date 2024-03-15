# Importing standard built-in random module for generating random numbers
import random

# Importing 'init' and 'Fore' functions from third-party colorama module
from colorama import init, Fore

# Initializing the colorama module for terminal color and style manipulation
init()


class WordList:
    """
    Class representing a WordList with a predefined list of words.
    """

    # Predefined list of words
    words = [
        'programming', 'development', 'algorithm', 'javascript', 'python',
        'software', 'function', 'variable', 'iteration', 'recursion',
        'database', 'framework', 'interface', 'inheritance', 'polymorphism',
        'abstraction', 'encapsulation', 'optimization', 'debugging', 'testing'
    ]

    @staticmethod
    def get_random_word():
        """
        Get a random word from the words list.

        This method retrieves a random word from the predefined list of words.

        Returns:
        - random_word: A randomly selected word from the words list.
        """
        # Use random.choice() function to select a random word from the list.
        return random.choice(WordList.words)


class GameMenu:
    def display_menu(self):
        """
        Display the main menu options for the game.

        This method prints the main menu options for the game, including:
        1. Hangman
        2. Scrambled Words
        3. Arithmetic Game
        4. Help
        5. Quit

        Returns:
        - None
        """
        # Print the game title.
        print(Fore.LIGHTWHITE_EX +
              " ╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌┬┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌─┐\n" +
              " ╠═╝└┬┘ │ ├─┤│ ││││││    ║ ╦├─┤│││├┤ └─┐\n" +
              " ╩   ┴  ┴ ┴ ┴└─┘┘└┘┴└─┘  ╚═╝┴ ┴┴ ┴└─┘└─┘")
        # Print the menu options.
        print(Fore.LIGHTCYAN_EX + "1. Hangman")
        print(Fore.LIGHTCYAN_EX + "2. Scrambled Words")
        print(Fore.LIGHTCYAN_EX + "3. Arithmetic Game")
        print(Fore.LIGHTCYAN_EX + "4. Help")
        print(Fore.LIGHTCYAN_EX + "5. Quit")

    def display_help(self):
        """
        Display the help screen with instructions on how to play each game.

        This method prints instructions on how to play each game.

        Returns:
        - None
        """
        print(Fore.LIGHTWHITE_EX + "Help Screen")
        print(Fore.LIGHTCYAN_EX + "Hangman: Guess the letters in the secret " +
                                  "word before you run out of guesses.")
        print(Fore.LIGHTCYAN_EX + "Scrambled Words: Unscramble the letters " +
                                  "to form the correct word.")
        print(Fore.LIGHTCYAN_EX + "Arithmetic Game: Answer arithmetic " +
                                  "questions correctly to score points.")

    def run(self):
        """
        Execute the main menu loop.

        This method executes the main menu loop. It displays the game menu,
        prompts the user for their choice, and executes the corresponding game
        or quits the program based on the user's input.

        Returns:
        - None
        """
        # Instantiate a WordList object to access word-related functionalities.
        word_list = WordList()

        # Main game loop
        while True:
            # Display the game menu.
            self.display_menu()

            # Prompt the user for their choice.
            choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice: \n")

            # Execute corresponding block of code based on the user's choice.
            if choice == "1":
                Hangman(word_list.get_random_word()).play()
            elif choice == "2":
                ScrambledWords(word_list.get_random_word()).play()
            elif choice == "3":
                ArithmeticGame().play()
            elif choice == "4":
                # Display the help screen.
                self.display_help()
            elif choice == "5":
                # If user chooses to quit, break out of the loop.
                print(Fore.LIGHTWHITE_EX + "Thank you for playing!")
                break
            else:
                # If user enters an invalid choice, display an error message.
                print(Fore.LIGHTRED_EX + "Invalid choice. Please try again.")


class Hangman:

    def __init__(self, word):
        """
        Initialize Hangman game with a secret word and initial guesses.

        This method initializes the Hangman game with a secret word, sets the
        initial number of guesses to 6, and initializes an empty set to store
        guessed letters.

        Parameters:
        - word: The secret word to be guessed.

        Returns:
        - None
        """
        # Store the secret word to be guessed.
        self.secret_word = word

        # Set the initial number of guesses.
        self.guesses_left = 6

        # Initialize an empty set to store guessed letters.
        self.guessed_letters = set()

    def display_word(self):
        """
        Display the current state of the word with guessed letters revealed.

        This method generates a string representing the current state of the
        secret word with guessed letters revealed and unguessed letters
        represented as underscores.

        Returns:
        - displayed_word: A string representing the state of the secret word.
        """
        # Initialize an empty string to store the displayed word.
        displayed_word = ''

        # Iterate through each letter in the secret word.
        for letter in self.secret_word:
            # If the letter has been guessed, append it to the displayed word.
            if letter in self.guessed_letters:
                displayed_word += letter
            # If the letter has not been guessed, append an underscore.
            else:
                displayed_word += '_'
        return displayed_word

    def guess_letter(self):
        """
        Prompt the player to guess a letter and validate the input.

        This method prompts the player to guess a letter. It validates the
        input to ensure that it is a single letter and has not been guessed
        before.

        Returns:
        - guess: The guessed letter.
        """
        # Loop until a valid guess is received.
        while True:
            guess = input(Fore.LIGHTYELLOW_EX + "Guess a letter: \n").lower()
            # Validate the input.
            if len(guess) != 1 or not guess.isalpha():
                print(Fore.LIGHTRED_EX + "Please enter a single letter.")
            elif guess in self.guessed_letters:
                print(Fore.LIGHTRED_EX + "You already guessed that letter.")
            else:
                return guess

    def play(self):
        """
        Execute the Hangman game.

        This method initiates the Hangman game. It displays the current state
        of the word, prompts the player to guess a letter, updates the guessed
        letters, and checks if the player has guessed the word correctly or run
        out of guesses.

        Returns:
        - None
        """
        # Display a welcome message for the Hangman game.
        print(Fore.LIGHTWHITE_EX + "Let's play Hangman!")

        # Main game loop
        while self.guesses_left > 0:
            # Display the current state of the word and remaining guesses.
            print(Fore.LIGHTCYAN_EX + "Word: " + self.display_word())
            print(Fore.LIGHTCYAN_EX + "Guesses left: " +
                                      str(self.guesses_left))

            # Prompt the player to guess a letter.
            guess = self.guess_letter()

            # Add the guessed letter to the set of guessed letters.
            self.guessed_letters.add(guess)

            # Check if the guessed letter is not in the secret word.
            if guess not in self.secret_word:
                self.guesses_left -= 1

            # Check if the player has guessed the entire word correctly.
            if self.display_word() == self.secret_word:
                print(Fore.LIGHTYELLOW_EX +
                      "Congratulations! You guessed the word: " +
                      self.secret_word)
                break
        else:
            # If the player runs out of guesses, display the correct word.
            print(Fore.LIGHTRED_EX +
                  "Sorry, you're out of guesses. The word was: " +
                  self.secret_word)