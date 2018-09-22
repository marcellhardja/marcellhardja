x = ""
time = int(input("Enter the time spent on the road: "))
time_for_distance = 0
acceleration = int(input("Enter the acceleration: "))
distance = int(input("Enter the distance: "))
speed_limit = 60
sym = "*"
stars = 0
speed = acceleration * time
goal_distance = acceleration * (time**2)


while time_for_distance<time:
    stars = (0.5*acceleration*(time_for_distance**2)/10)
    print ("Duration: "+ str(time_for_distance) + "Distance: " + (int(stars)*sym))
    time_for_distance +=1

if speed > 60:
    print ("the person went over the speed limit")

print ("Max speed was " +str(speed) +" m/s")

if goal_distance >= distance:
    print ("The person reached the destination. Reached " + str(goal_distance) + " m")
else:
    print("The person did not reach the destination. Reached "+ str(goal_distance) + " m")




