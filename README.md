# Python Mini Games

Small terminal games written in Python, originally school projects.

## Games

### Word Guess (`word_guess.py`)
The computer generates a random 5-letter string and you have 14 tries to guess
it. Correctly placed letters are revealed after each attempt.

### Number Guess (`number_guess.py`)
The computer picks a random 2-digit number (10-99) and you have 10 tries to find
it, with "higher" / "lower" hints after each guess. The interface is in French.

## Tech Stack
- Python (standard library only: `random`)

## Run
```
python word_guess.py
python number_guess.py
```

## Status
Old school projects, cleaned up later (fixed an answer leak and display-order
bug in Word Guess, added input validation to Number Guess).
