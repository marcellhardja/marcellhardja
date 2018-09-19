sym = "*"
count = int(input("Enter number for triangle size: "))
blank = " "
mult = 1

while mult<count:
    print (blank*(count-mult)+ sym*mult)
    mult += 1
