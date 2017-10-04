def main():

    word = input("Enter a word: ")
    newstr = ""   
    diff = ord('a') - ord('A')

    for ch in word:
        if ch >= 'a' and ch <= 'z':
            uppLetter = ord(ch) -  32
            newstr = newstr + chr(uppLetter)
        else:
            lowLetter = ord(ch) + 32
            newstr = newstr + chr(lowLetter)
    print(newstr)

main()
