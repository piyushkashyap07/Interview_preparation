def revPat(n):
    i=1
    while i <=n:
        j=1
        m=i
        while j<=i:
            print(m, end="")
            j+=1
            m-=1
        print()
        i+=1
        
    
if __name__ == "__main__":
    n= int(input("enter a number: "))
    revPat(n)
    
             