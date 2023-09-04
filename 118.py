p = int(input("enter the amount in rs:"))
t = int(input("enter in months:"))
r = 7.1
if p<500 or t<6:
    print("invalid")
else:    
    print(p*r*t/100)