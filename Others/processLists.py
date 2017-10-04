def interLeave(l1, l2):
    newList = []
    i, j = 0, 0
    while i < (len(l1)+len(l2)) and j < (len(l1)+len(l2)):
        if i < len(l1):
            newList.append(l1[i])
        if j < len(l2):
            newList.append(l2[j])
        i += 1
        j += 1
    print (newList)

        
def main():
    interLeave([7,18,9,13],[1,3,2])
    interLeave([2,1,8],[1,5,9,6,3])
    interLeave([34,41,28],[67,3,11])

main()
