# START
# GENERATE WORD AT RANDOM
# ASK USER TO GUESS A LETTER
# IS LETTER CORRECT -> YES - REPLACE BLANK WITH LETTER ->ARE ALL BLANKS FILLED -> YES - GAME OVER
#         |                                                           |-> N0 - GAME OVER
#         |-> NO - LOSE A LIFE -> RAN OUT OF LIVES -> YES - GAME OVER
#                                      |-> NO - REPEAT 4.


import os
import time
import random


word_list = ["apple", "calender", "mafia", "cat", "matchstick", "playoff", "earth", "black hole"]
chosen_word = random.choice(word_list)

hangman = ['''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
           ''', '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
           ''', '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
           ''', '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
           ''', '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
           ''', '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
           ''', '''
           +---+
           |   |
               |
               |
               |
               |
        =========
           ''']


display = []
for letter in chosen_word:
    display.append("_")
    
lives = 6
end_of_game = False

print(chosen_word)

while not end_of_game:
    
    guess = input("ENTER A LETTER: ").lower()

    os.system('cls')
    
    if guess in display:
        print("YOU HAVE ALREADY GUESSED THIS LETTER. ")
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        
        lives -=1
    print(hangman[lives])
    print(display)
    print(f"LIVES LEFT - {lives} ")
    
    if lives == 0 :
        end_of_game = True
        print("YOU LOSE.")
    if "_" not in display:
        end_of_game = True
        print("YOU WIN.")
        
time.sleep(5)