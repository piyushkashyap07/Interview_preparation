"""Problem statement

Send feedback
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= x <= 1,000
Sample Input 1 :
10
Sample Output 1 :
5 11 14 17 23 26 29 35 38 41
Sample Input 2 :
4
Sample Output 2 :
5 11 14 17
Explanation :
Input is 4 and print the first 4 numbers that are not divisible by 4 and are of the form 3N + 2, where k is a non-negative integer.   
Python (3.10)

Code pair




12
## Read input as specified in the question.## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
Console


Share your experience with this lecture?

"""

n = int(input())

count = 1 
current = 1

while(count <= n):
    num = 3 * current + 2
    
    if num % 4 != 0 :
    	print(num, end=" ")
    	count += 1

    current += 1
    