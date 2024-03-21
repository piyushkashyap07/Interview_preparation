def sqrPat(n):
    i=1
    while i <=n:
        j=1
        while j<=n:
            print(n, end="")
            j+=1
        print()
        i+=1
        
    
if __name__ == "__main__":
    n= int(input("enter a number: "))
    sqrPat(n)
    
             