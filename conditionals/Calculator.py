def calculator(n):
    
    while n!=6:
        if n==1:
            a = int(input("enter value of a: "))
            b = int(input("enter value of b: "))
            sum = a+b
            print(sum)
        if n==2:
            a = int(input("enter value of a: "))
            b = int(input("enter value of b: "))
            sub = a-b
            print(sub)
        if n==3:
            a = int(input("enter value of a: "))
            b = int(input("enter value of b: "))
            mul = a*b
            print(mul)
        if n==4:
            a = int(input("enter value of a: "))
            b = int(input("enter value of b: "))
            div = a/b
            print(div)
        if n==5:
            a = int(input("enter value of a: "))
            b = int(input("enter value of b: "))
            rem = a%b
            print(rem)
        if n>6 or n<0:
            print("Invalid Operation")
        n= int(input("ente a operator value: "))
            
if __name__ =="__main__":
    n= int(input("enter a number: "))
    calculator(n)