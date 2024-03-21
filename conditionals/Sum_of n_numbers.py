def sumOfNumber(n):
    sum  = 0
    for i in range(n+1):
        sum +=i
        
    return sum

if __name__ == "__main__":
    n = int(input())
    output = sumOfNumber(n)
    print(output)
    