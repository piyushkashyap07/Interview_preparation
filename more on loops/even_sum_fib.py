""" Even Fibonacci Numbers
Easy
Score
120/120
Average time to solve is 20m
Problem statement

Send feedback
Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N. Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
8
Sample Output 1 :
10
Sample Input 2:
400
Sample Output 2:
188"""



def sum_even_fib(n):
  sum = 0
  if(n<=1):
    return sum
  fib1, fib2 = 1, 1
  fib1, fib2 = fib2, fib1+fib2
  while(fib2<=n):
      if (fib2%2==0):
          sum += fib2
      fib1, fib2 = fib2, fib1+fib2
  return sum

print(sum_even_fib(int(input())))