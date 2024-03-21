def far_to_cel(s, e, steps):
    while s<=e:
        c=((s-32)*5)/9
        s+=steps
        print("farhenheight: ",s, "celcius: ", int(c))
    
    
    
    
if __name__ =="__main__":
    s=int(input("enter value of s: "))
    e=int(input("enter value of e: "))
    step=int(input("enter value of step: "))
    far_to_cel(s, e, step)