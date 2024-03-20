# Table of Contents

- [Pythonic Games](#pythonic-games)
  - [How to play and use Pythonic Games](#how-to-play-and-use-pythonic-games)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Data Model and Programming](#data-model-and-programming)
  - [Testing](#testing)
    - [Bugs and Issues](#bugs-and-issues)
    - [Remaining bugs](#remaining-bugs)
    - [Validator Testing](#validator-testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Other General Project Advice](#other-general-project-advice)

# Pythonic Games

Pythonic Games is a terminal-based Python games application designed to operate within the Code Institute mock terminal environment on Render. Pythonic Games extends a warm invitation to players through its menu system, where an assortment of games awaits exploration. The menu entices users with a plethora of options. Navigating through the menu is effortless, thanks to its intuitive design and user-friendly layout, allowing players to go from one game to another with just a few keystrokes. This accessibility underscores the mastery of Python programming, as Pythonic Games integrates the elegance and efficiency of the language, ensuring that gaming enjoyment is within reach for players of all ages and skill levels. Pythonic Games endeavors to enrich the lives of its target audience by offering a platform that fosters creativity, problem-solving skills, and endless hours of enjoyment in the realm of gaming.

Live link available at this location: [https://pythonic-games.onrender.com/](https://pythonic-games.onrender.com/)

![Pythonic Games](/readme/media/pythonic-games.png)

## How to play and use Pythonic Games

In the Pythonic Games application, a clear list of games is presented, players need only input the number associated with their desired game to initiate play.

When players select Hangman from the menu in Pythonic Games, they're prompted to input letters to uncover the hidden word, with the requirement to input one letter at a time.

When players opt for the Scrambled Words game, they're presented with a scrambled word that they must unscramble to reveal the correct word, with
players only having one opportunity to guess the correct word.

In the Arithmetic Game, players are presented with five mathematical calculations to solve after selecting the game from the menu. The objective is to solve each equation by inputting positive or negative numbers.

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

Inputting capital letters in the Scrambled Words game, as long as the word is correct, is accepted.

![Pythonic Games Scrambled Words Uppercase Input](/readme/media/pythonic-games-scrambled-words-uppercase-input.png)

The Arithmetic Game supports number input and requires whole numbers to be used.

![Pythonic Games Arithmetic Game Invalid Input](/readme/media/pythonic-games-arithmetic-game-invalid-input.png)

A score count is kept by the Arithmetic Game out of 5 points.

![Pythonic Games Arithmetic Game Score](/readme/media/pythonic-games-arithmetic-game-score.png)

Selecting the quit option on the game menu displays a `Thank you for playing` message

![Pythonic Games Menu Quit](/readme/media/pythonic-games-menu-quit.png)

### Future Features

Additional games could be incorporated into the Pythonic Games menu to offer users a wider variety of gaming options.

A more sophisticated points system could be integrated into Pythonic Games to measure precisely how well a player is doing.

Further development of the Pythonic Games application could involve integrating more advanced libraries with entirely new features.

## Data Model and Programming

Pythonic Games utilizes object-oriented programming and defines five classes and thirteen functions:

- `class WordList:`
  - `def get_random_word()`
- `class GameMenu`
  - `def display_menu(self)`
  - `def display_help(self)`
  - `def run(self):`
- `class Hangman`
  - `def __init__(self, word):`
  - `def display_word(self):`
  - `def guess_letter(self):`
  - `def play(self):`
- `class ScrambledWords`
  - `def __init__(self, word):`
  - `def scramble_word(self):`
  - `def play(self):`
- `class ArithmeticGame`
  - `def generate_question(self):`
  - `def play(self)`

Pythonic Games has a list of words that is used by both Hangman and Scrambled Words

-  `words = [
    'programming', 'development', 'algorithm', 'javascript', 'python',
    'software', 'function', 'variable', 'iteration', 'recursion',
    'database', 'framework', 'interface', 'inheritance', 'polymorphism',
    'abstraction', 'encapsulation', 'optimization', 'debugging', 'testing'
]`

Pythonic Games has four input prompts, one for the game menu and one for each of the three games.

- GameMenu
  - `choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice: \n"`

- Hangman
  - `guess = input(Fore.LIGHTYELLOW_EX + "Guess a letter: \n").lower()`

- ScrambledWords
  - `guess = input(Fore.LIGHTYELLOW_EX + "Your guess: \n")`

- ArithmeticGame
  - `user_answer = input(Fore.LIGHTCYAN_EX + question + "\n")`

The following flowchart provides an overview of the program's succinct functionality:

![Pythonic Games Flowchart](/readme/media/pythonic-games-flowchart.png)

## Testing

### Bugs and Issues

**EXTREMELY IMPORTANT INFORMATION: MUST READ**

This section will initially address the notable outages encountered by Codeanywhere and Heroku, the default platforms designated for this project. These outages resulted in the unavailability of these platforms to new users throughout the project's duration, contributing significantly to the project's complications. As this issue holds central importance in understanding the challenges faced by the project, it is essential to prioritize its discussion from the outset.

Countless hours were poured into the relentless pursuit of getting Codeanywhere and Heroku up and running. Specifically focusing on Heroku, these endeavors encompassed a multitude of strategies: from clearing cookies, trying various web browsers, and switching between different computers, to creating multiple email accounts across different service providers, utilizing VPN services, traveling to remote areas to access alternative internet providers, enlisting individuals globally to attempt account creation on my behalf, exhaustively tapping into all available tutoring and mentoring resources, personally reaching out to Heroku support, and even attempting to create accounts for uninterrupted stretches of 24 hours without sleep, among numerous other approaches. In essence, these efforts transcend comprehension.

It became increasingly clear that progress had ground to a halt and this despite all attempts. I received no response from Heroku support to any of my emails. I reached out to all accessible employees at the Code Institute for assistance. Regrettably, they expressed skepticism regarding the severity of the issue, citing that most students with pre-existing Heroku accounts had not encountered significant problems. Nevertheless, they diligently guided me through repeating all the troubleshooting steps, to which I readily complied.

In an effort to demonstrate the severity of the situation, I urged them to attempt the process themselves. Upon verifying that creating Heroku accounts was indeed unfeasible worldwide, they conferred with their team and granted me special authorization to use alternative platforms. They recommended Gitpod.io and Render to which I agreed. Subsequently, they advised me to notify the Code Institute via email of my decision to deploy on Render.

Faced with the challenge of mastering cloud platforms not included in my Learning Management System (LMS) due to the malfunctioning of Codeanywhere and Heroku, I realized this could significantly impede my learning journey. Moreover, it posed a risk of making the project unachievable, especially if intricate technical demands were involved. Anticipating potential obstacles, I approached The Code Institute to request any available documentation, recognizing the importance of being well-prepared for the hurdles that lay ahead.

Given that the assistance offered was not specifically designed for ordinary student use as Render usage is unusual, I found myself needing to extract as much pertinent information as possible from the Code Institute's internal usage documents. Of primary significance was obtaining the custom commands employed in Render, as outlined below.

![Pythonic Games Render commands](/readme/media/pythonic-games-render-commands.png)

Given my previous difficult experiences with cloud platforms, I was extremely careful to limit the amounts of times I would "build" a project in Render, as to not spend build-hours and find myself locked-out of a cloud platform, so I decided I would often leave manual deployment set in place. 

![Pythonic Games Render auto deploy no](/readme/media/pythonic-games-render-auto-deploy-no.png)

Pythonic Games underwent local testing using the standard command prompt.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-command-prompt.png)

The testing of Pythonic Games was also conducted locally using Windows PowerShell.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-powershell.png)

And of course the mock terminal on the Render platform in a web browser.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-render.png)

ChatGPT was utilized to automatically verify attainment of project objectives

![Pythonic Games ChatGPT](/readme/media/pythonic-games-chatgpt.png)

### Remaining bugs

Despite the absence of easy to find bugs within the program, several irregularities surfaced within the simulated terminal. Notably, pressing keys such as F1 through F12, insert, home, page up, del, end, page down, resulted in the generation of unexpected characters.

![Pythonic Games unexpected characters](/readme/media/pythonic-games-unexpected-characters.png)

Unfortunately, efforts to address these quirks were unsuccessful, as executing the same Python code outside of the simulated terminal failed to reproduce these anomalies. Moreover, adhering to instructions not to modify other files posed additional constraints.

![Pythonic Games do not edit files](/readme/media/pythonic-games-do-not-edit-files.png)

### Validator Testing

- PEP8
  - The CI Python Linter was used for validating adherence to PEP8 guidelines: [https://pep8ci.herokuapp.com/](https://pep8ci.herokuapp.com/)

Remark: Unfortunately, GitHub doesn't allow adding a newline at the end of the Python file.

![Pythonic Games CI Python Linter](/readme/media/pythonic-games-ci-python-linter.png)

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

- The Code Institute: [https://learn.codeinstitute.net/](https://learn.codeinstitute.net/)

  - The Learning Management System (LMS):
    - Python Essentials
    - Matt Rudge: Portfolio Project 3 Scope video: ULTIMATE BATTLESHIPS game: Information about project coding structure.
    - The template used in this project: [https://github.com/Code-Institute-Org/python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template)
    - README.md template from Portfolio Project Scope page.

  - James Stone: E-mailed template advice when at least two possible options existed.

  - Tutoring: Internal documents: Deployment to Render

  - Mentoring: Dick Vlaanderen: Project input validation verification, idea for the application help menu, Pycharm software lesson for docstrings, flow diagram lesson with a suggestion to use [https://app.diagrams.net/](https://app.diagrams.net/) or [https://miro.com/](https://miro.com/) and provided a starting diagram via e-mail.
  
- Ilyas Olgun [https://github.com/ilyasolgun11](https://github.com/ilyasolgun11) 

  - Suggested the following Text to ASCII Art Generator (TAAG) which was set to Calvin S to create the ASCII Pythonic Games logo:
[https://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=Pythonic%20Games](https://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=Pythonic%20Games)

  - Technical discussions about terminal command: `pip3 freeze > requirements.txt`

  - Discussed his GitHub projects, becoming an invaluable source of information.

- ChatGPT 3.5: [https://chat.openai.com/](https://chat.openai.com/)
  
  - Support for Python project:
    - Partial populating of text strings for the print() function.
    - Partial hash and docstring commenting, including the recommended format for docstrings, covering summary, description, parameters, return values, and examples.
    - Producing concise program examples to aid in exploring programming solutions. These examples were not meant for direct implementation, as they often include inaccuracies stemming from the generative AI process.
    - Partial verification of the project code's accuracy, not very succcesful but it inadvertently provided useful information as a side effect.
    - Partial support for README.md: Improving grammar and finding synonyms.

- Notepad ++: [https://notepad-plus-plus.org/](https://notepad-plus-plus.org/)

  - Code editor with higher execution speed and smaller program size.

- Python: [https://www.python.org/](https://www.python.org/)

  - The official home of the Python Programming Language.

- W3 Schools: [https://www.w3schools.com/python/](https://www.w3schools.com/python/)

  - Python Tutorial.

- YouTube: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

  - Harvard CS50’s Introduction to Programming with Python – Full University Course: [https://youtu.be/nLRL_NcnK-4](https://youtu.be/nLRL_NcnK-4)

- GitHub: [https://github.com/](https://github.com/)

  - Source code from over 100 million developers to learn from.

- Gitpod: [https://www.gitpod.io/](https://www.gitpod.io/)

  - Online integrated development environment (Online IDE)

- Render: [https://render.com/](https://render.com/)

  - Cloud platform for applications

## Other General Project Advice

- Diligent and thorough testing, characterized by unwavering attention to detail, is fundamental to mastering Python and progressing in its application development journey. This persistent quest to detect any signs of errors, anomalies, or areas for improvement is essential for refining one's skills and expertise with the language. Such rigorous testing serves as a cornerstone, providing a solid foundation upon which to build proficiency and tackle increasingly complex challenges in Python development.

- Collaborating and supporting fellow colleagues in their endeavors frequently fosters a culture of reciprocity, where they are inclined to reciprocate by offering valuable insights and information. This exchange of knowledge not only enriches both parties involved but also cultivates a sense of camaraderie within the workplace. The time saved through their assistance can be undeniably significant, contributing to increased efficiency and productivity in various tasks and projects.

- Securing deadline extensions due to technical outages is not only feasible but also highly advisable with appropriate justifications. In many cases, these extensions serve as crucial stress relievers, especially in light of the pervasive uncertainty surrounding the restoration of cloud platform services.