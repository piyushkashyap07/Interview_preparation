def intPat(n):
    i=1
    k=1
    while i <=n:
        j=1
        char= ord("A")+n-k
        while j<=i:
            print(chr(char), end="")
            j+=1
            char+=1
        print()
        i+=1
        k+=1
        
    
if __name__ == "__main__":
    n= int(input("enter a number: "))
    intPat(n)
    
             