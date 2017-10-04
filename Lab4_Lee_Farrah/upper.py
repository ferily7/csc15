def main():

    word = input("Enter a word: ")
    newstr = ""   
    diff = ord('a') - ord('A')

    for ch in word:
        if ch >= 'A' and ch <= 'Z' or ch == " ":
            newstr = newstr + ch
        else:
            uppLetter = ord(ch) - diff
            newstr = newstr + chr(uppLetter)
    print(newstr)

main()
