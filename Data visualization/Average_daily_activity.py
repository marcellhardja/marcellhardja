import csv
from matplotlib import pyplot as plt

def day_type(total_days):
    if total_days <= 7:
        if total_days <= 5:
            return "Weekday"
        else:
            return "Weekend"
    if total_days > 7:
        if total_days % 7 <= 4:
            return "Weekday"
        if total_days % 7 > 4:
            return "Weekend"

filename = 'C:\\Users\\user\\PycharmProjects\\Programming Exercise\\activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    interval = []
    average_interval = []
    steps = []
    days = []
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

    for i in range(0, 2356, 5):
        indexes = [k for k, x in enumerate(interval) if x ==i]
        values = 0

        for j in range(0, len(indexes)):
            values += steps[indexes[j]]

        values = values/len(set(days))
        average_interval.append(values)

print(average_interval)
print("The maximum number of steps is "+ str(int(max(average_interval)))+" in the "+str(average_interval.index(max(average_interval))*5)+ "th minutes")
intervals = [i for i in range(0 ,2356, 5)]
plt.plot(intervals, average_interval)
plt.ylabel("Averages")
plt.xlabel("Intervals")
plt.show()