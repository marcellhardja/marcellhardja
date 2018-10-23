import csv
import pygal
from datetime import datetime
import math as m

filename = 'C:\\Users\\user\\PycharmProjects\\Programming Exercise\\activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    day = []
    steps_per_day = []
    steps_total = 0
    total_days = 0
    total_steps = 0
    current_date = datetime.strptime("2012-10-01","%Y-%m-%d")
    step_number = []
    steps = []
    count = 0
    for x in reader:

        if str(x[0]) == "NA":
            step_number.append(0)
        else:
            step_number.append(int(x[0]))
        if current_date == datetime.strptime(x[1], "%Y-%m-%d"):
            steps_total += step_number[count]
            count+=1
        else:
            steps_per_day.append(steps_total)
            day.append(current_date)
            steps_total = 0
            current_date = datetime.strptime(x[1], "%Y-%m-%d")
            steps_total += step_number[count]
            count +=1


steps_per_day.append(steps_total)
day.append(current_date)
total_days=len(day)
total_steps=m.fsum(step_number)
meaner = int(total_steps / total_days)
sort = sorted(steps_per_day)
# print(sort)
print(steps_per_day)

hist = pygal.Bar()

hist.title= "Total number of steps taken per day."
hist.x_title = "Days"
hist._y_title = "Number of steps"

hist.add('Number of steps per day', steps_per_day)
hist.render_to_file('total_number_of_steps1.svg')

print("Total steps: " + str(total_steps))
print("Total days: " + str(total_days))
print("Average steps: " + str(meaner))
print("The Median: " + str(sort[30]))















