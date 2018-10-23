import csv
from matplotlib import pyplot as plt
import datetime as dt
def day_type(weekno):
    weekno = dt.datetime.strptime(weekno, "%Y-%m-%d")
    day = weekno.weekday()
    if day < 5:
        return "Weekday"
    else:
        return "Weekend"

def numberofdays(days, state):
    count = 0
    if state == "Weekdays":
        for i in range(0, len(days)):
            if day_type(days[i]) == "Weekday":
                count +=1

    elif state == "Weekends":
        for i in range(0, len(days)):
            if day_type(days[i]) == "Weekend":
                count +=1
    return count

filename = 'C:\\Users\\user\\PycharmProjects\\Programming Exercise\\activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    interval = []
    weekday_averages = []
    weekend_averages = []
    intervals = [i for i in range(0, 2356, 5)]
    count = 1
    steps = []
    days = []
    weekday = []
    weekend = []
    total_days = len(days)
    for x in reader:
        step = x[0]
        day = x[1]
        if step == "NA":
            steps.append(0)
            days.append(day)
            interval.append(x[2])
        else:
            steps.append(int(step))
            days.append(x[1])
            interval.append(int(x[2]))

wrkdays = set(days)
wrkdays = list(wrkdays)

weekends = numberofdays(wrkdays, "Weekends")
weekdays = numberofdays(wrkdays, "Weekdays")



for i in range(0, 2356, 5):
    indexes = [k for k, x in enumerate(interval) if x ==i]
    values = 0
    valueswknd = 0

    for j in range(0, len(indexes)):
        if day_type(days[indexes[j]]) == "Weekday":
            values += steps[indexes[j]]
        elif day_type(days[indexes[j]]) == "Weekend":
            values += steps[indexes[j]]

    values = values/weekdays
    valueswknd = values/weekends
    weekday_averages.append(values)
    weekend_averages.append(valueswknd)
    count += 1



weekday = plt.plot(intervals, weekday_averages, c = 'cyan')
weekend = plt.plot(intervals, weekend_averages, c = 'red')
plt.ylabel("Average Number of steps")
plt.xlabel("Minutes")
plt.legend(["Weekday Average", "Weekend average"])
plt.show()