""" Square Root (Integral)
Easy
Score
120/120
Average time to solve is 20m
Asked in companies
SamsungAdobeOracle
Problem statement

Send feedback
Given a number N, find its square root. You need to find and print only the integral part of square root of N.

For eg. if number given is 18, answer is 4.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^8
Sample Input 1 :
10
Sample Output 1 :
3
Sample Input 2 :
4
Sample Output 2 :
2"""






def sqrt(n):
    o=0
    while o*o <=n:
        o+=1
        
    o-=1
    return o


if __name__ =="__main__":
    n= int(input("enter a number n: "))
    output = sqrt(n)
    print(f"The squareRoot of the given number {n} is {output} 11in approximatioin.")