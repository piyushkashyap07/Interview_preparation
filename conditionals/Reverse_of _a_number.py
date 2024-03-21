def revNum(num):
    new_num = 0
    while num>0:
        rem = num%10
        num = num//10
        new_num = new_num*10 + rem
    return new_num

if __name__ =="__main__":
    n= int(input("enter a number: "))
    new_num = revNum(n)
    print(new_num)