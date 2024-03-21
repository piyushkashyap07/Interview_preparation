def reversenum(n):
    new_num = 0
    while n>0:
        rem =n%10
        n = n//10
        new_num = new_num*10+rem
    return new_num

def verify_pallindrome(n):
    rev_n = reversenum(n)
    if n ==rev_n:
        return "Yes"
    else:
        return "No"

if __name__ =="__main__":
    n = int(input("enter a number: "))
    output = verify_pallindrome(n)
    print(f"this number is {output} pallindrome!!!")