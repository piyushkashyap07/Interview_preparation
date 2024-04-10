def freq(n):
    d = {}
    max_freq = -1
    for i in n:
        d[i] = d.get(i, 0) + 1
    max_freq = -1
    key = -1
    for i in d:
        if d[i]> max_freq:
            max_freq = d[i]
            key = i 
    return key, max_freq

if __name__ == "__main__":
    n = [int(x) for x in input("Enter space-separated integers: ").split()]
    key, maximum_value = freq(n)
    print(f"The maximum frequency from the {key} is {maximum_value} in the dictionary.")
