def main():

    numList = [1,3, 5, 7, 5, 1, 10, 1]
    searchNum = eval(input("Enter a number to find: "))
    i = 0
    found = False

    while found == False and  i < len(numList):
        if searchNum == numList[i]:
            found = True
        else:
            i += 1

    if found == True:
        print("Number found!")
    else:
        print("Number not found!")
main()
