def main():
    
    #Initializing variables
    hangManSent = str(input("Enter a word: "))
    lowerStr = str.lower(hangManSent)
    parsedStr = lowerStr.replace(" ", "")
    bodyParts = ["head", "nose", "left ear", "right ear", "left eye", "right eye",
                 "mouth", "neck", "left arm", "right arm", "torso", "left leg", "right leg"]
    correctGuess = 0
    i = 0
    usedLetters = ""

    while correctGuess < len(parsedStr) and i < len(bodyParts):
        userGuess = input("Enter a letter: ")

        #Checks if the user entered the same letter
        if userGuess in usedLetters:
            print("You have guessed that letter already!")
        #Checks if the users guess is in the parsedStr
        elif parsedStr.count(userGuess) > 0:
            usedLetters = usedLetters + userGuess + ", "
            print("Found", parsedStr.count(userGuess), "occurrences of the letter",
                  userGuess, "in the sentence! \n" + "Letters used so far:", usedLetters)
            correctGuess += parsedStr.count(userGuess)
        #If the users guess is not in the parsedStr, it does this
        else:
            usedLetters = usedLetters + userGuess + ", "
            print("Sorry, that letter is not in the sentence. \n" + "You now have a",
                  bodyParts[i], "added to the hangman.")
            print("Letters used so far:", usedLetters)
            i += 1

    #Declaring if you win or lose the game
    if correctGuess == len(parsedStr):
        print("Yay, you win! :) The hangman sentence is:", hangManSent)
    else:
        print("Sorry, you lose! :(")
        
main()
