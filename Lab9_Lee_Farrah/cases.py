#This makes the word uppercase
def upper(upWord):

    newstr = ""   
    diff = ord('a') - ord('A')

    for ch in upWord:
        #This checks if the letter is already uppercase
        if ch >= 'A' and ch <= 'Z' or ch == " ":
            newstr = newstr + ch
        #This changes the letter to upper
        else:
            uppLetter = ord(ch) - diff
            newstr = newstr + chr(uppLetter)
    print(newstr)

#This makes the word lowercase
def lower(lowWord):

    newstr = "" 
    diff = ord('a') - ord('A')

    for ch in lowWord:
        #This checks if the letter is lowercase
        if ch >= 'a' and ch <= 'z' or ch == " ":
            newstr = newstr + ch
        #This changes the letter to lowercase
        else:
            lowLetter = ord(ch) + diff
            newstr = newstr + chr(lowLetter)
    print(newstr)

#This flips the case of the word.
def flip(flipWord):
    
    newstr = ""   
    diff = ord('a') - ord('A')

    for ch in flipWord:
        #If the letter is lowercase, it changes it to uppercase
        if ch >= 'a' and ch <= 'z':
            uppLetter = ord(ch) -  32
            newstr = newstr + chr(uppLetter)
        #If the letter is uppercase, it changes it to lowercase
        else:
            lowLetter = ord(ch) + 32
            newstr = newstr + chr(lowLetter)
    print(newstr)

def main():

    word = input("Enter a word: ")

    #Calls the functions
    upper(word)
    lower(word)
    flip(word)

main()
