def alphaPat(n):
    i=1
    m=ord("A")
    while i <=n:
        j=1
        while j<=i:
            print(chr(m), end="")
            j+=1
        m+=1
        print()
        i+=1
        
    
if __name__ == "__main__":
    n= int(input("enter a number: "))
    alphaPat(n)
    
             