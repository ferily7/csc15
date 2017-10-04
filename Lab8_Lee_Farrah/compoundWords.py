def main():

    #Reads the compountWord text file and makes it into a list
    infile = open("compoundWords.txt", "r")
    fileContents = infile.read()
    compoundList = fileContents.split("\n")

    #Initializes the variables
    correctGuesses = 0
    incorrectGuesses = 0
    numofTries = 0
    i = 0
    found = False

    print("Welcome to the game of compound words! I will present you with the first half of a compound word and you will guess the second half. You have three tries for every word. If you guess 5 words you win. If you get 5 words wrong, you lose. Good luck!")

    while correctGuesses < 5 and incorrectGuesses < 5 and i < len(compoundList):
        #This splits the compound words
        compoundWord = compoundList[i].split("-")

        print(compoundWord[0])
        userGuess = input("Enter your guess: ")

        #This checks if the user's guess is correct
        if userGuess == compoundWord[1]:
            correctGuesses += 1
            print("Correct! You have", correctGuesses, "words guessed already!")
        else:
            while numofTries < 3 and found == False:
                #for ch in compoundWord[1]:
                numofTries += 1
                print("Sorry, that's not the right word. Guess again with some hints.")
                print(compoundWord[0], str(compoundWord[1][0:numofTries]))

                if numofTries < 3:
                    guess = input("Enter another guess: ")
                #Checks if the user used all of its tries
                else:
                    incorrectGuesses += 1
                    print("Sorry, that's not the right word. The word was", compoundList[i])

                #Checks if the user's guess is correct
                if guess == compoundWord[1]:
                    found = True
                    correctGuesses += 1
                    print("Correct! You have", correctGuesses, "words guessed already!")

        i += 1
        numofTries = 0
        found = False

    #Determines if you win or lose
    if correctGuesses == 5:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")


main()
