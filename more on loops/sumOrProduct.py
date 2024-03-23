
"""Sum or Product
Easy
Score
120/120
Average time to solve is 20m
Problem statement

Send feedback
Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).



If C is equal to -
 1, then print the sum
 2, then print the product
 Any other number, then print '-1' (without the quotes)
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 12
Sample Input 1 :
10
1
Sample Output 1 :
55
Sample Input 2 :
10
2
Sample Output 2 :
3628800
Sample Input 3 :
10
4
Sample Output 3 :
-1"""

def sumorproduct(n,c):
    if c==1:
        sum=0
        for i in range(0, n+1):
            sum+=i
        print(sum)
    elif c==2:
        mul=1
        for i in range(1, n+1):
            mul*=i
        print(mul)
    else:
        print(-1)
        
if __name__=="__main__":
    n = int(input("Enter a number of n: "))
    c = int(input("Enter a number of C: "))
    sumorproduct(n, c)