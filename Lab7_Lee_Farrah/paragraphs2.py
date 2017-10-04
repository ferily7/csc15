def main():

    infile = open("paragraphs.txt", "r")
    fileContents = infile.read()
    counter = 1
    numSent = 0

    #134 words and 6 sentences
    for ch in fileContents:        
        if ch == " ":
            counter += 1
        elif ch == ".":
            numSent += 1
    print("Your sentence has", counter, "words and", numSent, "sentences.")

main()

