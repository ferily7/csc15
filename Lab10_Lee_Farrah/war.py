import random

def createDeck(deck):
    for i in range(len(deck)):
        for j in range(3):
            deck.append(deck[i])
    random.shuffle(deck)
    print (deck)
    
def distributeCards(deck, hand1, hand2):
    for i in range(int(len(deck)/2)):
        hand1.append(deck[i])
    for j in range(int(len(deck)/2),len(deck)):
        hand2.append(deck[j])
        
#def warGame(hand1, hand2):
    

#def gameOver(hand1, hand2):

def main():
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    hand1, hand2 = [], []
    createDeck(deck)
    distributeCards(deck, hand1, hand2)
main()
