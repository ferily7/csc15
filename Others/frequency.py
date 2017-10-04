def main():

    numList = [1,3, 5, 7, 5, 1, 10, 1]
    searchNum = eval(input("Enter a number to find: "))
    i = 0
    count = 0

    while i < len(numList):
        if searchNum == numList[i]:
            count += 1
            i += 1
        i += 1

    if count > 0:
        print("The number", searchNum, "appears", count, "times in", numList)
    else:
        print("Number not found!")

main()
