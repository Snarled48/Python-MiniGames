# Word-Guesse

A simple terminal-based guessing game in Python. The computer generates a random
5-letter string, and you have 14 tries to guess it, with correctly placed letters
revealed after each attempt.

## About
Built as a school project to practice loops, string manipulation, and basic
game-state tracking.

## Tech Stack
- Python (standard library only: `random`)

## How it works
1. A random 5-letter string is generated from uppercase letters
2. Each turn, you guess the full string (input is case-insensitive)
3. Correctly placed letters are revealed in a mask (e.g. `*A**O`)
4. You win by guessing it exactly, or lose after 14 tries

## Customizing
Change `WORD_LENGTH` and `MAX_TRIES` at the top of the file to make the game
easier or harder.

## Status
Old school project. Later cleaned up: removed an answer leak, fixed the display
order, and handled short or lowercase guesses.
