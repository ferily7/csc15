def main():

    sum = eval(input("Enter the number of terms to sum: "))


    for i in range(sum+1):

        if i > 0:
            value = float(((4/((2*i)-1))))
            print (value)


main()
