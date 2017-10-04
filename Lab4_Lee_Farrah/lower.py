def main():

    word = input("Enter a word: ")
    newstr = "" 
    diff = ord('a') - ord('A')

    for ch in word:
        if ch >= 'a' and ch <= 'z' or ch == " ":
            newstr = newstr + ch
        else:
            lowLetter = ord(ch) + diff
            newstr = newstr + chr(lowLetter)
    print(newstr)

main()
