# Pythonic Games

Pythonic Games is a terminal-based Python games application designed to operate within the Code Institute mock terminal environment on Render. Pythonic Games extends a warm invitation to players through its menu system, where an assortment of games awaits exploration. The menu entices users with a plethora of options. Navigating through the menu is effortless, thanks to its intuitive design and user-friendly layout, allowing players to go from one game to another with just a few keystrokes. This accessibility underscores the mastery of Python programming, as Pythonic Games integrates the elegance and efficiency of the language, ensuring that gaming enjoyment is within reach for players of all ages and skill levels. Pythonic Games endeavors to enrich the lives of its target audience by offering a platform that fosters creativity, problem-solving skills, and endless hours of enjoyment in the realm of gaming.

![Pythonic Games](/readme/media/pythonic-games.png)

## How to play and use Pythonic Games

In the Pythonic Games application, a clear list of games is presented, players need only input the number associated with their desired game to initiate play.

When players select Hangman from the menu in Pythonic Games, they're prompted to input letters to uncover the hidden word, with the requirement to input one letter at a time.

When players opt for the Scrambled Words game, they're presented with a scrambled word that they must unscramble to reveal the correct word, with
players only having one opportunity to guess the correct word.

In the Arithmetic Game, players are presented with five mathematical calculations to solve after selecting the game from the menu. The objective i to solve each equation by inputting positive or negative numbers.

Playing a selected game to completion is required in order to return to the main menu.

## Features

### Existing Features

The Pythonic Games application proudly presents its ASCII-art logo, adding a unique and visually captivating element to the user experience.

![Pythonic Games ASCII logo](/readme/media/pythonic-games-ascii-logo.png)

Pythonic Games offers a menu accessible by numeric selections, presenting the following options: Hangman, Scrambled Words, Arithmetic Game, Help, and Quit for users to choose from.

The Pythonic Games application displays its text using a variety of light Colorama colors (light white, light cyan, light yellow, light red) to improve the contrast with the Python mock terminal and allow users to distinguish easily between program text displays and inputs.

Both Hangman and Scrambled Words in Pythonic Games utilize a word list comprised of programming-related jargon intentionally chosen to educate users in programming concepts. This deliberate design choice serves as a valuable learning tool, familiarizing players with terminology commonly encountered in the realm of programming.

![Pythonic Games Jargon](/readme/media/pythonic-games-jargon.png)

The help screen within Python Games provides explanations for the various games available.

![Pythonic Games Help Screen](/readme/media/pythonic-games-help-screen.png)

Pythonic Games integrates input validation to deter the submission of erroneous input.

The robust menu programming code within Pythonic Games is designed to efficiently identify and handle invalid user input, ensuring smooth and error-free interaction with the program.

![Pythonic Games Menu Input Validation](/readme/media/pythonic-games-menu-input-validation.png)

Within Python Games, the hangman game is equipped to detect and handle invalid input, as well as repeated input, ensuring a seamless and error-free gaming experience.

![Pythonic Games Hangman Input Validation](/readme/media/pythonic-games-hangman-input-validation.png)

The Scrambled Words game, renowned for its extreme difficulty, will on purpose unveil the word even when submitting a blank entry, so it can serve as a quick surrender mechanism.
Inputting numbers as a word guess will however not be accepted.

![Pythonic Games Scrambled Words Blank Input](/readme/media/pythonic-games-scrambled-words-blank-input.png)

### Future Features

Additional games could be incorporated into the Pythonic Games menu to offer users a wider variety of gaming options.

A more sophisticated points system could be integrated into Pythonic Games to measure precisely how well a player is doing.

Further development of the Pythonic Games application could involve integrating more advanced libraries with entirely new features.

## Data Model

## Testing

### Bugs

### Remaining bugs

### Validator Testing

- PEP8
  - The CI Python Linter was used for validating adherence to PEP8 guidelines: [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)


## Deployment

This project was deployed using the Code Institute's mock terminal for Render.

- Steps for deployment:
  - Fork the Python Essentials Template of the Code Institute on Github:
  [https://github.com/Code-Institute-Org/python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template)
  - Create a new Web Service in Render
  - Build and deploy from a Git repository in Render
  - Connect the project Github repository in Render
  - Enter a unique name for the Web Service in Render
  - Region: Frankfurt (EU Central)
  - Branch: main
  - Runtime: Python 3
  - Build Command: pip install -r requirements.txt && npm install
  - Start Command: node index.js
  - Instance type: Free
  - Environmental Variables: PORT, 8000
  - Auto-Deploy: Yes
  - Click on Create Web Service

## Credits

## Other General Project Advice