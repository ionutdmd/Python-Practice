import random

from Hangman_words import word_list
from Hangman_art import stages

chosen_word = random.choice(word_list)
guess_word = "_" * len(chosen_word)

print("Welcome to HANGMAN!")
guesses = 6
while guesses > 0:
    print(guess_word)
    print(stages[guesses])
    letter = input("Please enter a letter: ").lower()
    if letter in guess_word:
        print(f"You've already guessed {letter}")
    elif letter in chosen_word:
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                guess_word = guess_word[:i] + letter + guess_word[i + 1:]
        print(guess_word)
        print("\n"*100)
        if chosen_word == guess_word:
            print("You won!!")
            break
    else:
        print(f"{letter} is not a letter in the chosen word. You have lost a life")
        guesses -= 1
        if guesses == 0:
            print("Out of guesses! You loose!!")
            print(stages[guesses])
            print(f"The word was {chosen_word}")
            break
        else:
            print(f"You have {guesses} guesses left. \n")
