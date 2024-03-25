"""All substrings
Moderate
Score
320/320
Average time to solve is 40m
Asked in companies
Ernst & Young (EY)SpringworksAppinventiv
Problem statement

Send feedback
For a given input string(str), write a function to print all the possible substrings.

Substring
A substring is a contiguous sequence of characters within a string. 
Example: "cod" is a substring of "coding". Whereas, "cdng" is not as the characters taken are not contiguous
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1:
abc
Sample Output 1:
a 
ab 
abc 
b 
bc 
c 
 Sample Input 2:
co
Sample Output 2:
c 
co 
o"""

def allString(s):
    for i in range(len(s)):
        j=i
        while j<len(s):
            print(s[i:j+1])
            j+=1
        
        
if __name__=="__main__":
    s = input("Enter a String: ")
    allString(s)
    