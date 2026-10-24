# Four Beginner-Friendly Python Projects

This repository contains four terminal-based Python projects for a beginner portfolio.

## Projects

1. **Hangman (`hangman.py`)** — randomly selected word, six wrong guesses, gallows stages, repeated-guess protection, replay option.
2. **Portfolio Tracker (`portfolio.py`)** — enter ticker, buy price, and whole-share quantity; calculates invested amount, sample market value, gain/loss and percentage; writes `portfolio_summary.csv`.
3. **File Organizer (`organizer.py`)** — sorts supported extensions into category folders. Preview mode is the default; confirm the proposed moves before running in live mode.
4. **Rule-Based Chatbot (`chatbot.py`)** — responds to greetings and common business FAQ intents, supports multiple intents and exit commands.

## Requirements

- Python 3.10 or newer recommended
- VS Code or another Python editor
- No third-party Python packages required

## Run in VS Code

Open this folder in VS Code. Open **Terminal → New Terminal** and run one command at a time:

```bash
python --version
python hangman.py
python portfolio.py
python organizer.py
python chatbot.py
```

On Windows, if `python` is not recognized, try `py` instead, for example `py hangman.py`.

### Portfolio sample data

`sample_prices.csv` contains example prices, not live stock prices. The prices are illustrative and can become outdated. The tracker does not make investment recommendations. It writes the latest run to `portfolio_summary.csv`.

### File organizer safety

First run `python organizer.py` and answer `y` to preview. Check the proposed destinations. Run again and answer `n` only when you are confident the folder path is correct. Try it on a temporary test folder first. It only checks files directly inside the chosen folder and does not recursively reorganize subfolders.

## Run tests

From the project folder:

```bash
python -m unittest -v
```

The tests use a temporary folder for file-organizer checks and do not move your real Downloads files.

## GitHub submission

1. Create a new **public** repository on GitHub, e.g. `python-four-projects`.
2. Do not initialize it with another README if you already have this README locally.
3. Open a terminal in this project folder and run:

```bash
git init
git add hangman.py portfolio.py organizer.py chatbot.py sample_prices.csv test_projects.py README.md
git commit -m "Add four Python beginner projects"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-four-projects.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username and use the actual repository URL. If Git asks you to sign in, complete the browser sign-in prompt. Do not upload passwords, access tokens, or private information.

Finally, open your GitHub repository in a browser, check that the files are visible, and submit the repository URL in the assignment portal.
