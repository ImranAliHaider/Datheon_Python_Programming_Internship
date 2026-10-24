# Datheon Python Programming Internship

## About This Repository

This repository contains four Python projects developed as part of the Datheon Python Programming Internship. The main purpose of these projects is to practice Python programming and apply basic programming concepts to real-world tasks.

Each project focuses on different skills, including conditional statements, loops, functions, file handling, CSV data processing, and basic problem-solving.

## 1. Hangman Game

### Project Description
Hangman is a word-guessing game in which the computer selects a hidden word and the player tries to guess it one letter at a time. The player must identify the correct word before running out of allowed attempts.

### How It Works
- The program selects a word from a predefined word list.
- The hidden word is displayed as underscores.
- The player enters one letter per guess.
- Correct guesses reveal the matching letters.
- Incorrect guesses reduce the remaining attempts.
- The game ends when the player guesses the word or runs out of attempts.

### Key Features
- Interactive command-line gameplay.
- Displays correctly guessed letters.
- Tracks incorrect guesses and remaining attempts.
- Prevents repeated guesses from unnecessarily reducing attempts.
- Shows a win or loss message at the end.

### Skills Practiced
Python variables, strings, lists, loops, conditional statements, and user input.

## 2. Stock Portfolio Tracker

### Project Description
The Stock Portfolio Tracker is a simple application that helps users understand the value of stock investments. It uses sample stock price data to calculate the investment cost and current market value of a portfolio.

### How It Works
- The program reads stock prices from a CSV file.
- It uses the portfolio's stock symbols, quantities, and purchase prices.
- It calculates the total amount invested.
- It calculates the current market value using the sample prices.
- It compares the investment cost with the market value.
- It saves a portfolio summary to a CSV file.

### Key Features
- Reads stock data from a CSV file.
- Calculates total investment and market value.
- Displays profit or loss based on the available sample data.
- Exports the portfolio summary for later use.

### Skills Practiced
Python functions, arithmetic operations, CSV file handling, data processing, and working with structured data.

**Note:** This project uses sample data for learning purposes. It does not provide live stock market prices or financial advice.

## 3. File Organizer

### Project Description
The File Organizer is a Python program that helps organize files in a folder. It sorts files into separate folders based on their extensions, making files easier to find and manage.

### How It Works
- The program checks the files inside a selected folder.
- It identifies file extensions, such as `.pdf`, `.jpg`, `.png`, and `.txt`.
- It determines the appropriate folder for each file type.
- It can show a preview of the planned changes before moving files.
- When the user runs it in organizing mode, files are moved into the relevant folders.

### Key Features
- Automatically groups files by extension.
- Creates folders for different file types when needed.
- Includes a preview mode to check planned changes.
- Handles duplicate filenames to help avoid overwriting existing files.

### Skills Practiced
Python file handling, directories, paths, loops, conditional statements, and the `os` and `shutil` modules.

**Note:** Always check the target folder before moving files. Preview mode is useful for verifying the changes first.

## 4. Rule-Based Chatbot

### Project Description
The Rule-Based Chatbot is a simple conversational program that responds to user messages using predefined rules and keywords. It demonstrates how a basic chatbot can recognize common questions and provide suitable responses.

### How It Works
- The chatbot asks the user to enter a message.
- It checks the message against predefined words or patterns.
- It selects a response based on the detected intent.
- It continues responding until the user enters the exit command.

### Key Features
- Responds to common greetings and questions.
- Uses predefined responses and matching rules.
- Recognizes certain message patterns.
- Supports repeated conversations through a command-line interface.
- Provides a simple exit option.

### Skills Practiced
Python strings, functions, loops, conditional statements, regular expressions, and basic text processing.

**Note:** This is a rule-based chatbot, not an AI model trained on a large dataset. Its responses depend on the rules defined in the code.

## Technologies Used

- **Programming Language:** Python 3
- **Data Handling:** CSV files
- **File Management:** Python file and directory operations
- **Text Processing:** String operations and regular expressions
- **Testing:** Python unit testing

## Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code, or a terminal.
- Any additional libraries required by an individual project.

## How to Run the Projects

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code or a terminal.
3. Open the terminal in the project directory.
4. Run the Python file you want to use.

### Run Hangman Game
```bash
python hangman.py
```

### Run Stock Portfolio Tracker
```bash
python portfolio.py
```

### Run File Organizer
```bash
python organizer.py
```

### Run Rule-Based Chatbot
```bash
python chatbot.py
```

Use `python3` instead of `python` if that is the command used by your system.

## Testing

The repository includes a test file named `test_projects.py`. You can run the tests with:

```bash
python -m unittest test_projects.py
```

The tests help check selected project functions and expected behavior.

## Learning Outcomes

By completing these projects, I practiced:
- Writing and organizing Python code.
- Using loops, conditions, and functions.
- Working with files, folders, and CSV data.
- Handling user input and program output.
- Testing program behavior.
- Solving basic programming problems through practical projects.

## Conclusion

These projects represent my practical learning during the Datheon Python Programming Internship. They helped me strengthen my Python fundamentals and understand how programming can be used to build small, useful applications.

**Internship:** Datheon Python Programming Internship  
**Language:** Python 3


