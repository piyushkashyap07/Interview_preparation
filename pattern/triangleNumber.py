"""Pattern: Triangle of numbers
Moderate
Score
240/240
Average time to solve is 40m
Asked in companies
DunzoHCL TechnologiesTata Consultancy Services (TCS)
Problem statement

Send feedback
Print the following pattern for the given number of rows.

Pattern for N = 4



The dots represent spaces.




Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
          232
         34543
        4567654
       567898765
Sample Input 2:
4
Sample Output 2:
           1
          232
         34543
        4567654"""
        
        
def triangleNumbers(n):
    i=1
    
    while i<=n:
        s=1
        while s<=n-i:
            print(" ",end="")
            s+=1
        num=i  
        while num<=2*i-1:
            print(num, end="")
            num+=1
        j=2*i-2
        j_=1
        while j_<=i-1 and j!=0:
            print(j,end="")
            j+=1
            j_+=1
        
        i+=1
        print()

if __name__=="__main__":
    n= int(input("enter a number: "))
    triangleNumbers(n)
    
    