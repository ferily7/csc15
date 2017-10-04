import urllib.request

def main():

    #Importing the list of words from the URL
    wordsURL = "http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt"
    urlInput = urllib.request.urlopen(wordsURL).read()
    words = urlInput.decode('utf-8')

    #Creating file names and writing the list of words to the file
    outfile = open("words.txt", "w")
    outfile.write(words)
#    outfile.close()
    infile = open("words.txt", "r")
    outfile = open("nameUpper.txt", "w")

    upperStr = ""

    #This makes all of the words in the list uppercase
    for line in infile:
        upperStr += line.upper()
    outfile.write(upperStr)


main()
