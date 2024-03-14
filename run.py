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
        