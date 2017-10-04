def interLeave(l1, l2):
    newList = []
    j = 0
    for i in range((len(l1)+len(l2))):
        if i < len(l1):
            newList.append(l1[i])
        if j < len(l2):
            newList.append(l2[j])
        j += 1
    print (newList)

        
def main():
    interLeave([7,18,9,13],[1,3,2])
    interLeave([2,1,8],[1,5,9,6,3])
    interLeave([34,41,28],[67,3,11])

main()
