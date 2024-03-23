"""Decimal to Binary
Moderate
Score
240/240
Average time to solve is 40m
Problem statement

Send feedback
Given a decimal number (integer N), convert it into binary and print.

Note for C++ coders:
Do not use the inbuilt implementation of "pow" function. The implementation of that function is done for 'double's and it may fail when used for 'int's, 'long's, or 'long long's. Implement your own "pow" function to work for non-float data types. 
The given input number could be large, so the corresponding binary number can exceed the integer range. So you may want to take the answer as long for CPP and Java. 


Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 10^5
Sample Input 1 :
12
Sample Output 1 :
1100
Sample Input 2 :
7
Sample Output 2 :
111
Sample Input 2 :
0
Sample Output 2 :
0
"""


def decTobin(n):
    sum=0
    i=1
    while n>0:
        temp =n%2
        sum+=i*temp
        n//=2
        i*=10
    return sum


if __name__ =="__main__":
    n=int(input("enter a number: "))
    binary = decTobin(n)
    print(binary)
    
        
        