speed = int(input("What is the speed of the vehicle in mph?"))
time = int(input("How many hours has it traveled?"))
x=1
while x <= time:
	distance = speed * x
	print ("at " + str(x) + "hours, the distance is " + str(distance))
	x += 1
