"""Trailing zeroes in n!
Moderate
Score
240/240
Average time to solve is 40m
Problem statement

Send feedback
Find and return number of trailing 0s in n factorial without calculating n factorial.

Sample Input
50
Sample Output
12
Input Size Limit
n < 10^11"""
def tellZeoro(n):
    i =0
    while n>0:
        if n%5==0:
            i+=1
        n//=5
    return i
        

def trailingzeroes(n):
    if n==0:
        return 1
    sum=0
    for i in range(0, n+1, 5):
        sum+=tellZeoro(i)
    return sum


if __name__ =="__main__":
    n =int(input("enter a number: "))
    zeroes = trailingzeroes(n)
    print(zeroes)
    
    