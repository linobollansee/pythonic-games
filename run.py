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