def main():

    word = input("Enter a word: ")
    counter = 0
    
    for ch in word:
        if (ch  == 'a'  or ch == 'e' or ch == 'i' or ch == 'o' or ch =='u' \
or ch == 'A'  or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            counter = counter + 1
    print("The word you entered has" , counter, "vowels.")

main()
