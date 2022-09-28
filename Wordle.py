# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():



    def get_guess(row):
        # currentRow = gw.get_current_row()
        currentGuess = ''
        for i in range(5):
            currentGuess += gw.get_square_letter(row, i)
        return currentGuess

    def enter_action(s):

        currentGuess = get_guess(0)
        print(currentGuess)

        gw.set_square_color(0,0,'green')
        gw.set_square_color(0,1,'yellow')
        gw.set_square_color(0,2,'grey')

        # Increment current row, needs logic for end of game
        gw.set_current_row(gw.get_current_row() + 1)

        # Check if user filled out five letters
        # Check if entered word is actual word (optional)
        # Trigger comparison logic of entered and wordToGuess
        # Update GUI and move on to next round or terminate game


    # On game start select a random word from our word list
    randIndex = random.randint(0, len(FIVE_LETTER_WORDS))
    wordToGuess = FIVE_LETTER_WORDS[randIndex]
    print(wordToGuess)

    gw = WordleGWindow()
    gw.show_message("Enter your guess!")
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
