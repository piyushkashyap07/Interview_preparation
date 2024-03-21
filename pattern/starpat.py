def starpattern(n):
    
    i=1
    while i<=n:
        s=1
        while s<=n-i:
            print(" ", end="")
            s+=1
            
        num=1
        while num<=i:
            print("*",end="")
            num+=1
        j=1
        while j<=i-1:
            print("*",end="")
            j+=1
        i+=1
        print()

if __name__ == "__main__":
    n= int(input("enter a number: "))
    starpattern(n)
    
    