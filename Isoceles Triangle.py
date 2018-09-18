sym = ("*")
space = (" ")
mult = 1
tf = 1
while tf == 1:
    count = int(input("Enter diamond size "))
    if count%2 > 0:
        tf = 0

while mult <= count:
    print (space*((count-mult)/2)+sym*mult+space*((count-mult)/2))
    mult += 2

mult -= 2
while mult >= 1:
    print (space*((count-mult)/2)+sym*mult+space*((count-mult)/2))
    mult -= 2
