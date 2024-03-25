"""String Palindrome
Easy
Score
160/160
Average time to solve is 20m
Asked in companies
Publicis SapientTata Consultancy Services (TCS)Adobe
Problem statement

Send feedback
Given a string, determine if it is a palindrome, considering only alphanumeric characters.

Palindrome
A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
Example:
If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards, it is said to be a valid palindrome.

The expected output for this example will print, 'true'.
From that being said, you are required to return a boolean value from the function that has been asked to implement.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= N <= 10^6
Where N is the length of the input string.

Time Limit: 1 second
Sample Input 1 :
abcdcba
Sample Output 1 :
true 
Sample Input 2:
coding
Sample Output 2:
false"""


def checkpallindrome(s):
    i =0
    j=len(s)-1
    
    while i<j:
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1
    return True

if __name__ =="__main__":
    s = input("Enter a String: ")
    output = checkpallindrome(s)
    if output:
        print(f"The given String is pallindrome!!!")
    else:
        print("The given String is not a pallindrome!!!")