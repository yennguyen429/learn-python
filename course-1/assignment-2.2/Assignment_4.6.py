def computepay(h,r):
    if h > 40:
        pay = (40*r) + (h-40)*(1.5*r)
    else: 
        pay = h*r
    return pay
h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
pay = computepay(h,r)
print("Pay", pay)
