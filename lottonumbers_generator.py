import random
import datetime

combinations = []
true_combination = []
start = 1
ends = 0
count = 1
limit = 6

x = datetime.datetime.now()
day = x.strftime("%A")
print("Today is {}".format(day))

if day == "Monday" or day == "Wednesday" or day == "Saturday":
    ends = 55

elif day == "Tuesday" or day == "Friday" or day == "Sunday":
    ends = 58

elif day == "Thursday":
    ends = 49

while count <= limit:
    i = random.randint(start, ends)
    combinations.append(i)
    if i not in true_combination:
        true_combination.append(i)

    else:
        limit += 1

    count += 1

print(true_combination)
