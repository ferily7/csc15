def main():

    sent  = input("Enter a sentence: ")
    counter = 0
    numSent = 0
    
    for ch in sent:
        if ch == " ":
            counter = counter + 1
        elif ch == ".":
            numSent = numSent +1
    print("Your sentence has", counter+1, "words and", numSent, "sentences.")

main()

