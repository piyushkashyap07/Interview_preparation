def sumOfEven(n):
    sum_even = 0
    for i in range(n+1):
        if i%2==0:
            sum_even +=i
    return sum_even


if __name__ == "__main__":
    n = int(input("enter a number: "))
    output = sumOfEven(n)
    print(output)