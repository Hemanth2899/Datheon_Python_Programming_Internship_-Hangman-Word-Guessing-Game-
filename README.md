# Datheon_Python_Programming_Internship_-Hangman-Word-Guessing-Game-
A simple Python-based Hangman word-guessing game featuring random word selection, ASCII graphics, six attempts, duplicate guess handling, and replay functionality. It downloads a word list when available and uses built-in words offline. This project demonstrates Python fundamentals, functions, loops, conditionals, sets, and file handling.
🎮 Python Hangman Game

📌 Project Description

The Python Hangman Game is a simple, interactive word-guessing game developed using Python. The player must guess a hidden word by entering one letter at a time. The player has six incorrect attempts to find the correct word before the game ends.

🎯 Objectives

- Practice basic Python programming.
- Understand loops, conditional statements, and functions.
- Learn how to use sets and file handling.
- Develop a simple interactive console-based game.

✨ Features

- Random selection of words.
- Six incorrect attempts per game.
- ASCII art showing the Hangman stages.
- Displays correctly guessed and incorrect letters.
- Prevents duplicate guesses without penalty.
- Downloads an English word list and saves it locally.
- Uses built-in words if the download fails.
- Option to play again after each round.

🛠️ Technologies Used

- Python 3
- Random module
- OS module
- urllib.request module

📂 Project Structure

Python-Hangman-Game/
│
├── hangman.py
├── words.txt
└── README.md

Note: "words.txt" is created automatically when the word list downloads successfully. It is not required because the program includes fallback words.

⚙️ Requirements

- Python 3 installed on your computer.
- Internet connection for downloading the word list (optional).

▶️ How to Run the Project

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

python hangman.py

4. Wait for the game to display the hidden word.
5. Enter one letter at a time.
6. Guess the complete word before using all six incorrect attempts.
7. Choose "y" to play again or "n" to exit.

🎮 How to Play

- The game randomly selects a secret word.
- The letters of the word are initially hidden.
- Enter a single letter as your guess.
- Correct guesses reveal the matching letters.
- Incorrect guesses reduce the remaining attempts.
- Repeated guesses do not count as incorrect attempts.
- You win by guessing all the letters before your attempts run out.

📚 Concepts Learned

- Variables and data types
- Functions and loops
- Conditional statements
- Sets and string manipulation
- File handling
- Exception handling
- Random word selection
- User input validation

🚀 Future Improvements

- Add difficulty levels.
- Include categories such as technology, science, and sports.
- Create a graphical user interface (GUI).
- Add a score system and leaderboard.
- Track wins and losses.

👨‍💻 Author

Hemanth

📄 License

This project is open for learning and educational purposes.
