def checkNumber(number):
    if number==0:
        print("Zero")
    elif number>0:
        print("Positive")
    else:
        print("Negative")
        
        
if __name__ == "__main__":
    n =  int(input("Enter a Number: "))
    checkNumber(n)