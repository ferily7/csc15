#This functions changes the list from string to integer
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    

#This function squares each number in the list
def squareEach(nums):
    squareList = []
    for n in range(len(nums)):
        nums[n] = nums[n] * nums[n]    

#This function gets the sum of the squared numbers in the list
def sumList(nums):
    sum1 = 0
    for n in nums:
        sum1 = sum1 + n
    return sum1

def main():
    #Reads the sumList text file and makes it into a list
    infile = open("sumList.txt", "r")
    fileContents = infile.read()
    numList = fileContents.split(", ")

    toNumbers(numList)
    squareEach(numList)
    squaredSum = sumList(numList)
    print("The sum of the list is:", squaredSum)

    

main()
