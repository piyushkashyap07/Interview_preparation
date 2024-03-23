"""Binary to decimal
Easy
Score
120/120
Average time to solve is 20m
Asked in companies
SnapdealSamsungAccenture
Problem statement

Send feedback
Given a binary number as an integer N, convert it into decimal and print.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^9
Sample Input 1 :
1100
Sample Output 1 :
12
Sample Input 2 :
111
Sample Output 2 :
7"""


def binGToDec(n):
    sum=0
    i=0
    while n>0:
        temp = n%2
        if temp==1:
            sum+=2**i
            n//=10
            i+=1
        else:
            n//=10
            i+=1
    return sum
        
        
if __name__ =="__main__":
    n = int(input("Enter a number: "))
    dec = binGToDec(n)
    print(dec)
