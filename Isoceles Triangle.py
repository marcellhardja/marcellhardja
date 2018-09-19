sym = ("*")
space = (" ")
mult = 1
x = 1
while x == 1:
    count = int(input("Enter triangle size: "))
    if count%2 > 0:
        x=0
    else:
        print("Enter an odd number")

while mult <= count:
    print (space*((count-mult)/2)+sym*mult+space*((count-mult)/2))
    mult += 2
