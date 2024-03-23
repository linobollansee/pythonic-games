# Table of Contents

- [Pythonic Games](#pythonic-games)
  - [Deployed project](#deployed-project)
  - [Proof-of-concept before deployment](#proof-of-concept-before-deployment)
  - [How to play and use Pythonic Games](#how-to-play-and-use-pythonic-games)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Pythonic Games ASCII-art logo](#pythonic-games-ascii-art-logo)
      - [Pythonic Games Menu](#pythonic-games-menu)
      - [Pythonic Games Colors](#pythonic-games-colors)
      - [Pythonic Games Word List](#pythonic-games-word-list)
      - [Pythonic Games Menu Input Validation](#pythonic-games-menu-input-validation)
      - [Pythonic Games Hangman Input Validation](#pythonic-games-hangman-input-validation)
      - [Pythonic Games Scrambled Words Input Validation](#pythonic-games-scrambled-words-input-validation)
      - [Pythonic Games Arithmetic Game Input Validation](#pythonic-games-arithmetic-game-input-validation)
      - [Pythonic Games Arithmetic Game Score](#pythonic-games-arithmetic-game-score)
      - [Pythonic Games Help Screen](#pythonic-games-help-screen)
      - [Pythonic Games Quit Option](#pythonic-games-quit-option)
    - [Future Features](#future-features)
  - [Data Model and Programming](#data-model-and-programming)
    - [Pythonic Games Object-Oriented Programming](#pythonic-games-object-oriented-programming)
    - [Pythonic Games Word List](#pythonic-games-word-list)
    - [Pythonic Games Input Prompts](#pythonic-games-input-prompts)
    - [Pythonic Games Flowchart](#pythonic-games-flowchart)
    - [Pythonic Games Libraries](#pythonic-games-libraries)
  - [Bugs and Issues](#bugs-and-issues)
    - [Codeanywhere and Heroku outages](#codeanywhere-and-heroku-outages)
    - [PEP8 errors](#pep8-errors)
    - [Cloud IDE errors](#cloud-ide-errors)
    - [Command pip3 freeze](#command-pip3-freeze)
    - [Remaining bugs](#remaining-bugs)
  - [Testing](#testing)   
    - [Command-line interfaces](#command-line-interfaces)
    - [Artificial intelligence verification](#artificial-intelligence-verification)
    - [Browser compatibility](#browser-compatibility)
    - [Screenshot mirroring](#screenshot-mirroring)
    - [Validator Testing](#validator-testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Other General Project Advice](#other-general-project-advice)

# Pythonic Games

Pythonic Games is a terminal-based Python games application designed to operate within the Code Institute mock terminal environment on Render. Pythonic Games extends a warm invitation to players through its menu system, where an assortment of games awaits exploration. The menu entices users with a plethora of options. Navigating through the menu is effortless, thanks to its intuitive design and user-friendly layout, allowing players to go from one game to another with just a few keystrokes. This accessibility underscores the mastery of Python programming, as Pythonic Games integrates the elegance and efficiency of the language, ensuring that gaming enjoyment is within reach for players of all ages and skill levels. Pythonic Games endeavors to enrich the lives of its target audience by offering a platform that fosters creativity, problem-solving skills, and endless hours of enjoyment in the realm of gaming.

Live link available at this location: [https://pythonic-games.onrender.com/](https://pythonic-games.onrender.com/)

## Deployed project

![Pythonic Games](/readme/media/pythonic-games.png)

## Proof-of-concept before deployment

![Pythonic Games](/readme/media/pythonic-games-proof-of-concept.png)

## How to play and use Pythonic Games

In the Pythonic Games application, a clear list of games is presented, players need only input the number associated with their desired game to initiate play.

When players select Hangman from the menu in Pythonic Games, they're prompted to input letters to uncover the hidden word, with the requirement to input one letter at a time.

When players opt for the Scrambled Words game, they're presented with a scrambled word that they must unscramble to reveal the correct word, with
players only having one opportunity to guess the correct word.

In the Arithmetic Game, players are presented with five mathematical calculations to solve after selecting the game from the menu. The objective is to solve each equation by inputting positive or negative numbers.

When the user chooses the Help option from the menu, the game explanations will be shown.

Selecting the Quit option from the menu causes the program to end.

Playing a selected game to completion is required in order to return to the main menu.

## Features

### Existing Features

#### Pythonic Games ASCII-art logo

The Pythonic Games application proudly presents its ASCII-art logo, adding a unique and visually captivating element to the user experience.

![Pythonic Games ASCII logo](/readme/media/pythonic-games-ascii-logo.png)

#### Pythonic Games Menu

Pythonic Games offers a menu accessible by numeric selections, presenting the following options: Hangman, Scrambled Words, Arithmetic Game, Help, and Quit for users to choose from.

![Pythonic Games Menu](/readme/media/pythonic-games-menu.png)

#### Pythonic Games Colors

The Pythonic Games application displays its text using a variety of light Colorama colors (light white, light cyan, light yellow, light red) to improve the contrast with the Python mock terminal and allow users to distinguish easily between program text displays and inputs.

#### Pythonic Games Word List

Both Hangman and Scrambled Words in Pythonic Games utilize a word list comprised of programming-related jargon intentionally chosen to educate users in programming concepts. This deliberate design choice serves as a valuable learning tool, familiarizing players with terminology commonly encountered in the realm of programming.

![Pythonic Games Jargon](/readme/media/pythonic-games-jargon.png)

#### Pythonic Games Menu Input Validation

Pythonic Games integrates input validation to deter the submission of erroneous input.

The robust menu programming code within Pythonic Games is designed to efficiently identify and handle invalid user input, ensuring smooth and error-free interaction with the program.

![Pythonic Games Menu Input Validation](/readme/media/pythonic-games-menu-input-validation.png)

Within Python Games, the hangman game is equipped to detect and handle invalid input, as well as repeated input, ensuring a seamless and error-free gaming experience.

#### Pythonic Games Hangman Input Validation

![Pythonic Games Hangman Input Validation](/readme/media/pythonic-games-hangman-input-validation.png)

#### Pythonic Games Scrambled Words Input Validation

The Scrambled Words game, renowned for its extreme difficulty, will on purpose unveil the word even when submitting a blank entry or wrong answer, so these can serve as a quick surrender mechanism for a user that has tried to complete the word and given up. Inputting numbers as a word guess will however not be accepted.

![Pythonic Games Scrambled Words Blank Input](/readme/media/pythonic-games-scrambled-words-blank-input.png)

Inputting capital letters in the Scrambled Words game, as long as the word is correct, is accepted.

![Pythonic Games Scrambled Words Uppercase Input](/readme/media/pythonic-games-scrambled-words-uppercase-input.png)

#### Pythonic Games Arithmetic Game Input Validation

The Arithmetic Game supports number input and requires whole numbers to be used.

![Pythonic Games Arithmetic Game Invalid Input](/readme/media/pythonic-games-arithmetic-game-invalid-input.png)

#### Pythonic Games Arithmetic Game Score

A score count is kept by the Arithmetic Game out of 5 points.

![Pythonic Games Arithmetic Game Score](/readme/media/pythonic-games-arithmetic-game-score.png)

#### Pythonic Games Help Screen

The help screen within Python Games provides explanations for the various games available.

![Pythonic Games Help Screen](/readme/media/pythonic-games-help-screen.png)

#### Pythonic Games Quit Option

Selecting the quit option on the game menu displays a `Thank you for playing` message

![Pythonic Games Menu Quit](/readme/media/pythonic-games-menu-quit.png)

### Future Features

Additional games could be incorporated into the Pythonic Games menu to offer users a wider variety of gaming options.

A more sophisticated points system could be integrated into Pythonic Games to measure precisely how well a player is doing.

Further development of the Pythonic Games application could involve integrating more advanced libraries with entirely new features.

## Data Model and Programming

### Pythonic Games Object-Oriented Programming

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

### Pythonic Games Word List

Pythonic Games has a list of words that is used by both Hangman and Scrambled Words

-  `words = [
    'programming', 'development', 'algorithm', 'javascript', 'python',
    'software', 'function', 'variable', 'iteration', 'recursion',
    'database', 'framework', 'interface', 'inheritance', 'polymorphism',
    'abstraction', 'encapsulation', 'optimization', 'debugging', 'testing'
]`

### Pythonic Games Input Prompts

Pythonic Games has four input prompts, one for the game menu and one for each of the three games.

- GameMenu
  - `choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice: \n"`

- Hangman
  - `guess = input(Fore.LIGHTYELLOW_EX + "Guess a letter: \n").lower()`

- ScrambledWords
  - `guess = input(Fore.LIGHTYELLOW_EX + "Your guess: \n")`

- ArithmeticGame
  - `user_answer = input(Fore.LIGHTCYAN_EX + question + "\n")`

#### Pythonic Games Flowchart

The following flowchart provides an overview of the program's succinct functionality:

![Pythonic Games Flowchart](/readme/media/pythonic-games-flowchart.png)

### Pythonic Games Libraries

Pythonic-games import the built-in random module for generating random numbers.

-  `import random`

Pythonic-Games imports the third-party colorama library in Python.

- `from colorama import init, Fore`

This package simplifies printing colored text in terminals.

## Bugs and Issues

### Codeanywhere and Heroku outages

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

### PEP8 errors

To correct PEP8 errors, Pythonic Games used string concatenation to seperate long print lines into multiple shorter lines.

![Pythonic Games String Concatenation](/readme/media/pythonic-games-string-concatenation.png)

### Cloud IDE errors

At times, Gitpod.io experienced malfunctions. In response, GitHub Codespaces was utilized, offering superior performance compared to other cloud IDEs synchronized with GitHub. Additionally, it was discovered that pressing the comma key after selecting a repository provided a quicker route to Codespaces.

### Command pip3 freeze

Although using `pip3 freeze > requirements.txt` may seem like an easy way to update the requirements.txt file with Python packages, its effectiveness can differ depending on the integrated development environment (IDE) being used. For instance, in Gitpod.io, it did not add any packages at all. Conversely, in GitHub Codespaces, it excessively added 135 packages, making manual addition of packages a better approach. For documentation purposes, here are the packages that GitHub Codespaces added, most of which are not used by this project:

```
anyio==4.3.0
argon2-cffi==23.1.0`
argon2-cffi-bindings==21.2.0
arrow==1.3.0
asttokens==2.4.1
async-lru==2.0.4
attrs==23.2.0
Babel==2.14.0
beautifulsoup4==4.12.3
bleach==6.1.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
colorama==0.4.6
comm==0.2.1
contourpy==1.2.0
cycler==0.12.1
debugpy==1.8.1
decorator==5.1.1
defusedxml==0.7.1
exceptiongroup==1.2.0
executing==2.0.1
fastjsonschema==2.19.1
filelock==3.13.1
fonttools==4.49.0
fqdn==1.5.1
fsspec==2024.2.0
gitdb==4.0.11
GitPython==3.1.42
h11==0.14.0
httpcore==1.0.4
httpx==0.27.0
idna==3.6
ipykernel==6.29.3
ipython==8.22.2
isoduration==20.11.0
jedi==0.19.1
Jinja2==3.1.3
joblib==1.3.2
json5==0.9.20
jsonpointer==2.4
jsonschema==4.21.1
jsonschema-specifications==2023.12.1
jupyter-events==0.9.0
jupyter-lsp==2.2.4
jupyter-server-mathjax==0.2.6
jupyter_client==8.6.0
jupyter_core==5.7.1
jupyter_server==2.13.0
jupyter_server_terminals==0.5.2
jupyterlab==4.1.3
jupyterlab_git==0.50.0
jupyterlab_pygments==0.3.0
jupyterlab_server==2.25.3
kiwisolver==1.4.5
MarkupSafe==2.1.5
matplotlib==3.8.3
matplotlib-inline==0.1.6
mistune==3.0.2
mpmath==1.3.0
nbclient==0.9.0
nbconvert==7.16.2
nbdime==4.0.1
nbformat==5.9.2
nest-asyncio==1.6.0
networkx==3.2.1
notebook_shim==0.2.4
numpy==1.26.4
nvidia-cublas-cu12==12.1.3.1
nvidia-cuda-cupti-cu12==12.1.105
nvidia-cuda-nvrtc-cu12==12.1.105
nvidia-cuda-runtime-cu12==12.1.105
nvidia-cudnn-cu12==8.9.2.26
nvidia-cufft-cu12==11.0.2.54
nvidia-curand-cu12==10.3.2.106
nvidia-cusolver-cu12==11.4.5.107
nvidia-cusparse-cu12==12.1.0.106
nvidia-nccl-cu12==2.19.3
nvidia-nvjitlink-cu12==12.3.101
nvidia-nvtx-cu12==12.1.105
overrides==7.7.0
packaging==23.2
pandas==2.2.1
pandocfilters==1.5.1
parso==0.8.3
pexpect==4.9.0
pillow==10.2.0
platformdirs==4.2.0
plotly==5.19.0
prometheus_client==0.20.0
prompt-toolkit==3.0.43
psutil==5.9.8
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.21
Pygments==2.17.2
pyparsing==3.1.1
python-dateutil==2.9.0.post0
python-json-logger==2.0.7
pytz==2024.1
PyYAML==6.0.1
pyzmq==25.1.2
referencing==0.33.0
requests==2.31.0
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rpds-py==0.18.0
scikit-learn==1.4.1.post1
scipy==1.12.0
seaborn==0.13.2
Send2Trash==1.8.2
six==1.16.0
smmap==5.0.1
sniffio==1.3.1
soupsieve==2.5
stack-data==0.6.3
sympy==1.12
tenacity==8.2.3
terminado==0.18.0
threadpoolctl==3.3.0
tinycss2==1.2.1
tomli==2.0.1
torch==2.2.1
tornado==6.4
traitlets==5.14.1
triton==2.2.0
types-python-dateutil==2.8.19.20240106
typing_extensions==4.10.0
tzdata==2024.1
uri-template==1.3.0
urllib3==2.0.7
wcwidth==0.2.13
webcolors==1.13
webencodings==0.5.1
websocket-client==1.7.0
```

Remark: Only the colorama package is needed by this project.

### Remaining bugs

Despite the absence of easy to find bugs within the program, several irregularities surfaced within the simulated terminal. Notably, pressing keys such as F1 through F12, insert, home, page up, del, end, page down, resulted in the generation of unexpected characters.

![Pythonic Games unexpected characters](/readme/media/pythonic-games-unexpected-characters.png)

Unfortunately, efforts to address these quirks were unsuccessful, as executing the same Python code outside of the simulated terminal failed to reproduce these anomalies. Moreover, adhering to instructions not to modify other files posed additional constraints.

![Pythonic Games do not edit files](/readme/media/pythonic-games-do-not-edit-files.png)

## Testing

### Command-line interfaces

Pythonic Games underwent local testing using the standard command prompt.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-command-prompt.png)

The testing of Pythonic Games was also conducted locally using Windows PowerShell.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-powershell.png)

And of course the mock terminal on the Render platform in a web browser.

![Pythonic Games Command Prompt](/readme/media/pythonic-games-render.png)

### Artificial intelligence verification

ChatGPT was utilized to automatically verify attainment of project objectives

![Pythonic Games ChatGPT](/readme/media/pythonic-games-chatgpt.png)

### Browser compatibility

The deployed site of Pythonic Games was play-tested on Google Chrome, Microsoft Edge, Mozilla Firefox, and no errors were detected.

Google Chrome Version 123.0.6312.59 (Official Build) (64-bit)

![Pythonic Games Google Chrome](/readme/media/pythonic-games-google-chrome.png)

Microsoft Edge Version 123.0.2420.53 (Official build) (64-bit)

![Pythonic Games Microsoft Edge Chrome](/readme/media/pythonic-games-microsoft-edge.png)

Mozilla Firefox 124.0.1 (64-bit)

![Pythonic Games Mozilla Firefox](/readme/media/pythonic-games-mozilla-firefox.png)

### Screenshot mirroring

Remark: Pythonic Games has undergone thorough testing. However, due to numerous test image screenshots mirroring those already present in existing features, they will not be replicated here.

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
    ![Pythonic Games Portfolio Project 3 Scope Video](/readme/media/pythonic-games-portfolio-project-3-scope-video.png)
    - The template used in this project: [https://github.com/Code-Institute-Org/python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template)
    - README.md template from Portfolio Project Scope page.
    ![Pythonic Games Portfolio Project Scope README](/readme/media/pythonic-games-portfolio-project-scope-readme.png)

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
    ![Pythonic Games ChatGPT Hangman Messages Displayed To Player](/readme/media/pythonic-games-chatgpt-hangman-messages-displayed-to-player.png)
    - Partial hash and docstring commenting, including the recommended format for docstrings, covering summary, description, parameters, return values, and examples.
    ![Pythonic Games Google Docstrings](/readme/media/pythonic-games-chatgpt-google-docstrings.png)
    - Producing concise program examples to aid in exploring programming solutions. Unfortunately, many of them are not suited for direct implementation, as they often include inaccuracies stemming from the generative AI process, but if the questions are kept simple
    the quality of the assistance can remain acceptable. See an interaction here:
    ![Pythonic Games ChatGPT String Methods](/readme/media/pythonic-games-chatgpt-string-methods.png)
    This approach can save syntax lookup-time at as little risk as possible.
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

  - GitHub Codespaces: [https://github.com/codespaces](https://github.com/codespaces)

- Gitpod: [https://www.gitpod.io/](https://www.gitpod.io/)

  - Online integrated development environment (Online IDE)

- Render: [https://render.com/](https://render.com/)

  - Cloud platform for applications

- Balsamiq Wireframes: [https://balsamiq.com/](https://balsamiq.com/)

  - Wireframing tool used for designing the proof-of-concept

## Other General Project Advice

- Diligent and thorough testing, characterized by unwavering attention to detail, is fundamental to mastering Python and progressing in its application development journey. This persistent quest to detect any signs of errors, anomalies, or areas for improvement is essential for refining one's skills and expertise with the language. Such rigorous testing serves as a cornerstone, providing a solid foundation upon which to build proficiency and tackle increasingly complex challenges in Python development.

- Collaborating and supporting fellow colleagues in their endeavors frequently fosters a culture of reciprocity, where they are inclined to reciprocate by offering valuable insights and information. This exchange of knowledge not only enriches both parties involved but also cultivates a sense of camaraderie within the workplace. The time saved through their assistance can be undeniably significant, contributing to increased efficiency and productivity in various tasks and projects.

- Securing deadline extensions due to technical outages is not only feasible but also highly advisable with appropriate justifications. In many cases, these extensions serve as crucial stress relievers, especially in light of the pervasive uncertainty surrounding the restoration of cloud platform services.

- Continuously expanding one's knowledge and skills through ongoing learning and professional development opportunities is crucial for staying abreast of advancements in Python and related technologies. Whether through online courses, workshops, or participation in open-source projects, investing in personal growth ensures that developers remain competitive and adaptable in today's rapidly evolving tech landscape.

-  Considering the inherent challenges involved in creating easily comprehensible commit messages for meticulously debugged Python code, it is strongly advised to allocate extra time towards thoroughly verifying the code before its initial commitment. This proactive approach not only minimizes the occurrence of unnecessary fixes within the repository but also ensures the perpetuation of clear and concise commit messages, contributing to the overall cleanliness and coherence of the project's version history.