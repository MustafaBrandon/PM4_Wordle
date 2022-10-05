# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from asyncio.windows_events import NULL
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():



    def winFunction(row):
        print("got here")
        gw.set_square_color(0,0,'green')
        gw.set_square_color(0,1,'green')
        gw.set_square_color(0,2,'green')
        gw.set_square_color(0,3,'green')
        gw.set_square_color(0,4,'green')

        #you won the game
        gw.show_message("That is correct!")




    def get_guess(row):
        # currentRow = gw.get_current_row()
        currentGuess = ''
        for i in range(5):
            currentLetter = gw.get_square_letter(row, i)
            #if currentLetter is blank, then don't add it to the currentGuess
            if currentLetter == ' ':
                currentGuess = currentGuess
            else:
                 currentGuess += gw.get_square_letter(row, i)
        return currentGuess

    def enter_action(s):

        #this needs to be incremented after each guess that meets the criteria (5 letters, in the dictionary)
        currentGuess = get_guess(0)
        currentGuess= currentGuess.lower()
        
        #get current length, if it's not 5 then break out of this function and don't increment the row
        if len(currentGuess) == 5:

            #check if lower case word is in the dictionary, if not, show message saying word is not in dictionary
            if currentGuess.lower() in FIVE_LETTER_WORDS:
                
                # if word is correct

                if currentGuess.lower() == wordToGuess:
                    winFunction("row")


                #guess logic 
                wordToGuessList = list(wordToGuess)
                print(wordToGuessList)
                for letter in currentGuess:
                    if letter in wordToGuessList:
                        indexGuess = currentGuess.index(letter)

                        #account for possiblity of multiple letters in word
                        indexAnswer = []
                        for i in range(len(wordToGuessList)):
                                if wordToGuessList[i] == i:
                                    indexAnswer.append(i)

                        print(indexAnswer)
                        print(indexGuess)
                        
                        #if the indexes are equal, then correct posisiton, color it green

                        #account for multipleof same letter in the word
                        for multipleLetters in indexAnswer:
                            if indexGuess == indexAnswer:
                                gw.set_square_color(0,indexGuess,"#66BB66")

                            #if not equal, but there is a result, then it is yellow
                            elif indexGuess != indexAnswer:
                                gw.set_square_color(0,indexGuess,"#CCBB66")


                        #else, color gray
                    else:
                        indexGuess = currentGuess.index(letter)
                        gw.set_square_color(0,indexGuess,"#999999")



                #break guessed word  into list of letters
                #break answer word into list of letters
                # compare letters in guessed word to correct word


                #color the correct letters

                #increment to next line

                # gw.set_square_color(0,0,'green')
                # gw.set_square_color(0,1,'yellow')
                # gw.set_square_color(0,2,'grey')

                # Increment current row, needs logic for end of game
                gw.set_current_row(gw.get_current_row() + 1)
                
                # Check if entered word is actual word (optional)
                # Trigger comparison logic of entered and wordToGuess
                # Update GUI and move on to next round or terminate game
                
            else:
                gw.show_message("Word not in dictionary")

                

        else:
            gw.show_message("You must enter a 5 letter word")

            


    # On game start select a random word from our word list
    randIndex = random.randint(0, len(FIVE_LETTER_WORDS))
    wordToGuess = FIVE_LETTER_WORDS[randIndex]
    print(wordToGuess)

    gw = WordleGWindow()
    gw.show_message("Enter your guess!")
    gw.add_enter_listener(enter_action)



#function to compare 


# Startup code

if __name__ == "__main__":
    wordle()
