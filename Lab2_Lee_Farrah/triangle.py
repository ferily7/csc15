def main():
    
    size = int(input("Enter a number"))

    
    for i in range(size+1):
        if i > 0:
            print ((" " * (size-i)) , ("*" * ((2*i)-1)))
        
main()



