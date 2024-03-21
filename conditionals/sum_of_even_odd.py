def sum_even_odd_loop(n):
    sum_even =0
    sum_odd =0
    
    for i in range(n+1):
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
            
    return sum_even, sum_odd

def sum_even_odd(n):
    temp = n
    sum_even = 0
    sum_odd = 0
    while temp>0:
        rem = temp%10
        temp =temp//10
        if rem%2==0:
            sum_even+=rem 
        else:
            sum_odd+=rem
            
    return sum_even, sum_odd
            

if __name__ =="__main__":
    n = int(input("enter a number: "))
    even, odd = sum_even_odd(n)
    print("even sum: ", even, "odd sum: ", odd)