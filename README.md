# Hangman-Project
This project is a Hangman Game implemented in Python. Players attempt to guess a randomly chosen word by guessing letters one at a time. The game provides visual feedback on the player's progress and tracks lives lost for incorrect guesses. It uses modular components like word lists and ASCII art to enhance gameplay.

# Steps to Create the Project:
## 1. Project Initialization

### a. Created a new Python project for the Hangman Game.
### b. Set up modularity by separating the ASCII art and word list into dedicated modules (hangman_art.py and hangman_words.py).

## 2. Building the Word Selection Logic

### a. Defined a list of words in hangman_words.py for the game to randomly select from.
### b. Used the random module to pick a random word at the start of each game.

## 3. Game Setup

### a. Initialized key variables in the main script:
1. lives to track the number of incorrect guesses allowed.
2. placeholder to display the current progress of the word being guessed.
3. correct_letters to store correctly guessed letters.

## 4. Player Interaction

### a. Implemented a loop to prompt the user to guess letters until the game ends.
### b. Added validation to ensure the player doesn't guess the same letter multiple times.

## 5. Game Mechanics

### a. Checked each guessed letter against the randomly chosen word:
### b. Updated the placeholder if the letter was correct.
### c. Deducted a life if the letter was incorrect.
### d. Used ASCII art from hangman_art.py to visually display the hangman stages based on lives left.

## 6. Win/Loss Conditions

### a. Added conditions to check for a win (all letters guessed) or a loss (lives reduced to zero).
### b. Displayed appropriate messages for both outcomes, including the correct word if the player lost.

## 7. Game Testing and Refinement

### a. Tested the game to handle edge cases, such as invalid inputs or repeated guesses.
### b. Improved the user experience by providing helpful feedback and clear prompts.

## 8. Final Touches

### a. Integrated the ASCII art logo at the start of the game for a welcoming experience.
### b.Ensured the code was modular and easy to extend or modify.
