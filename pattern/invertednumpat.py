def inv_num_pat(n):
    i=0
    m=n
    while i<=n:
        j=1
        while j<=n-i:
            print(m,end="")
            j+=1
        print()
        i+=1
        m-=1
    

if __name__=="__main__":
    n= int(input("enter a number: "))
    inv_num_pat(n)