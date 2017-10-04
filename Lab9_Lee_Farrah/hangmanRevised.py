#This function initializes all the variables and returns them
def init():
    hangManSent = str(input("Enter a word: "))
    lowerStr = str.lower(hangManSent)
    parsedStr = lowerStr.replace(" ", "")
    bodyParts = ["head", "nose", "left ear", "right ear", "left eye", "right eye",
                 "mouth", "neck", "left arm", "right arm", "torso", "left leg", "right leg"]
    correctGuess = 0
    i = 0
    usedLetters = []
    return hangManSent, lowerStr, parsedStr, bodyParts, correctGuess, i, usedLetters

    
#This function checks if the user's guess is correct
def correctGuesses(parseStr, guess, useLetters, correctGuesses):
    if parseStr.count(guess) > 0:
        useLetters.append(guess)
        print("Found", parseStr.count(guess), "occurrences of the letter",
              guess, "in the sentence!")
        correctGuesses += parseStr.count(guess)
    return correctGuesses

#This function checks if the user's guess is incorrect
def incorrectGuess(parseStr, useLetters, guess, bodyPartsList, i):
    if guess not in parseStr:
        useLetters.append(guess)
        print("Sorry, that letter is not in the sentence. \n" + "You now have a",
              bodyPartsList[i], "added to the hangman.")
        i += 1
    return i

#This function declares if the user won or lost the game
def WinorLose(correctGuesses, parseStr, sentence):
    if correctGuesses == len(parseStr):
        print("Yay, you win! :) The hangman sentence is:", sentence)
    else:
        print("Sorry, you lose! :(")

def main():
    
    #Initializing variables
    hangManSent, lowerStr, parsedStr, bodyParts, correctGuess, i, usedLetters = init()

    while correctGuess < len(parsedStr) and i < len(bodyParts):
        userGuess = input("Enter a letter: ")

        #This checks if the user entered the same letter
        if userGuess in usedLetters:
            print("You have guessed that letter already!")
        #If the same letter is not found, declares the function
        else:
            correctGuess = correctGuesses(parsedStr, userGuess, usedLetters, correctGuess)
            i = incorrectGuess(parsedStr, usedLetters, userGuess, bodyParts, i)

        print("Letters used so far:", usedLetters)

    WinorLose(correctGuess, parsedStr, hangManSent)
        
main()
