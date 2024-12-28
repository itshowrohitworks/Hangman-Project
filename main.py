import random
from hangman_art import logo

print("Welcome to the Hangman Game with Python!")
print(logo)

# Generate Random Word from List of Word:
from hangman_words import word_list
random_word = random.choice(word_list)


# Player:
from hangman_art import stages
lives = 6


# Replace position of every letter in Random Word with placeholder:
placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
print("\n")    

# While the game is not over User guesses an Input letter:
game_over = False
correct_letters = []
while not game_over:
    print(f"************************** You've left {lives} Lives Left **************************")
    guess = input("Guess a letter: ")

    if guess in correct_letters:
        print(f"You've already guessed {display}")



# If the letter in Random Word is same as user guess put it in display, if not print "_":
    display = ""
    for letter in random_word:
        if letter == guess.lower():
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in random_word:
        lives -= 1
        print(f"You've guessed {guess}, thats not in the Word, You Lose a life!")


        if lives == 0:
            game_over = True
            print(f"************************** It was {random_word}, You lose! **************************")
    
    if "_" not in display:
        game_over = True
        print("************************** You Win! **************************")

    print(stages[lives])