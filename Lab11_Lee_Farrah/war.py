import random

#This fuction is adding exactly 4 of each card and randomizing the deck
def createDeck():
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    for i in range(len(deck)):
        for j in range(3):
            deck.append(deck[i])
    random.shuffle(deck)
    return deck
    
#This fuction is splitting the deck in half for Player 1 and 2
def distributeCards(deck):
    hand1, hand2 = [], []
    for i in range(int(len(deck)/2)):
        hand1.append(deck[i])
    for j in range(int(len(deck)/2),len(deck)):
        hand2.append(deck[j])
    return hand1, hand2

#This function changes the numeric value of the card to the proper value
def convertNumericVals(card):
    if card == 1:
        card = "Ace"
    elif card == 11:
        card = "Jack"
    elif card == 12:
        card = "Queen"
    elif card == 13:
        card = "King"
    return card

#This function takes the two cards and adds it to the winner's deck
def processDeck(hand, card1, card2):
    hand.append(card1)
    hand.append(card2)

#This processes the whole War round
def WarRound(hand1, hand2, card1, card2):
        
    print("*****************************THIS IS WAR!!**********************************")
    warDeck = []
    count = 1
    win = False
    doubleTie = False
    i = 0

    while win == False:
        #This if statement checks if the player's hand is less than 4 when a War is declared
        if len(hand1) == 0:
            hand2.append(card1)
            hand2.append(card2)
            win = True
        elif len(hand2) == 0:
            hand2.append(card1)
            hand2.append(card2)
            win = True
        elif len(hand1) < 4:
            if len(hand1) == 3:
                for i in range(3): 
                    hand2.append(hand1.pop(0))
                hand2.append(card1)
                hand2.append(card2)
            elif len(hand1) == 2:
                for i in range(2):
                    hand2.append(hand1.pop(0))
                hand2.append(card1)
                hand2.append(card2)
            elif len(hand1) == 1:
                hand2.append(hand1.pop(0))
                hand2.append(card1)
                hand2.append(card2)
            win = True
        elif len(hand2) < 4:
            if len(hand2) == 3:
                for i in range(3):
                    hand1.append(hand2.pop(0))
                hand1.append(card1)
                hand1.append(card2)
            elif len(hand2) == 2:
                for i in range(2):
                    hand1.append(hand2.pop(0))
                hand1.append(card1)
                hand1.append(card2)
            elif len(hand2) == 1: 
                hand1.append(hand2.pop(0))
                hand1.append(card1)
                hand1.append(card2)
            win = True
        #This statement if a 2nd war is declared and a player's hand is less than 4
        if doubleTie == True:
            if len(hand1) < 4:
                hand2.extend(warDeck)
            elif len(hand2) < 4:
                hand1.extend(warDeck)

        while win == False and doubleTie == False:                
            for i in range(3):
                warDeck.append(hand1.pop(0))
                warDeck.append(hand2.pop(0))
                print("Player 1 and 2 draw", count, "card face down.")
                count += 1
                i += 1
    
            warDeck.append(card1)
            warDeck.append(card2)
                
            warCard1 = hand1.pop(0)
            warCard2 = hand2.pop(0)
            convertCard1 = convertNumericVals(warCard1)
            convertCard2 = convertNumericVals(warCard2)
            print("Player 1 draws last card", convertCard1, "-", "Player 2 draws last card", convertCard2)
            i = 0
            count = 1
    
            #Processing who wins the War round and gains the cards
            if warCard1 != warCard2:
                if (warCard1 > warCard2 and warCard2 != 1) or (warCard1 == 1 and warCard2 != 2) or (warCard1 == 2 and warCard2 ==1):
                    hand1.extend(warDeck)
                    hand1.append(warCard1)
                    hand1.append(warCard2)
                    print("Player 1 wins the cards!")
                elif (warCard2 > warCard1 and warCard1 != 1) or (warCard2 == 1 and warCard1 != 2) or (warCard2 == 2 and warCard1 == 1):
                    hand2.extend(warDeck)
                    hand2.append(warCard1)
                    hand2.append(warCard2)
                    print("Player 2 wins the cards!")
                win = True
            #This statement is declared if there is a second war
            elif warCard1 == warCard2 and (len(hand1) < 4 or len(hand2) < 4):
                doubleTie = True    

#This checks who wins the round
def winnerOfRound(hand1, hand2, card1, card2):
    if (card1 > card2 and card2 != 1) or (card1 == 1 and card2 != 2) or (card1 == 2 and card2 ==1):
        processDeck(hand1, card1, card2)
        print("Player 1 wins the cards!")
    elif (card2 > card1 and card1 != 1)or (card2 == 1 and card1 != 2) or (card2 == 2 and card1 == 1):
        processDeck(hand2, card1, card2)
        print("Player 2 wins the cards!")
    else:
        WarRound(hand1, hand2, card1, card2)
    print("Player 1 has", len(hand1), "cards - Player 2 has", len(hand2), "cards")

#Process of the War game and contains all the functions
def warGame(hand1, hand2):
    while len(hand1) > 0 and len(hand2) > 0:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)
        convertCard1 = convertNumericVals(card1)
        convertCard2 = convertNumericVals(card2)
        print("Player 1 draws", convertCard1, "-", "Player 2 draws", convertCard2)
        winnerOfRound(hand1, hand2, card1, card2)
    gameOver(hand1, hand2)
    
#This declares who won the War game
def gameOver(hand1, hand2):
    print("Game Over!!!")
    
    if len(hand1) == 0:
        print("Player 2 wins the game!!")
    elif len(hand2) == 0:
        print("Player 1 wins the game!!")

#Main function that decalres other functions
def main():
    deck = createDeck()
    hand1, hand2 = distributeCards(deck)
    warGame(hand1, hand2)
main()
