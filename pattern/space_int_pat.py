def space_pat(n):
    # space
    # s=1
    i=1
    while i<=n:
        s=1
        while s<=n-i:
            print(" ",end="")
            s+=1
        num=1
        while num <=i:
            print(num,end="")
            num+=1
        print()
        i+=1
    pass

if __name__=="__main__":
    n= int(input("enter a number: "))
    space_pat(n)