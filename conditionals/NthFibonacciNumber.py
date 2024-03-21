def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Parameters:
        n (int): The index of the Fibonacci number to generate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    a = 0
    b = 1
    c = 0

    for i in range(n):
        c = a + b
        a = b
        b = c 

    return a

if __name__ == "__main__":
    n = int(input("Enter the index of the Fibonacci number: "))
    print(f"The Fibonacci number at index {n} is {fibonacci(n)}.")
