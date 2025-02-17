# Time
print("--------Task #1: 'Time'--------")
minutes_total = 808
print(minutes_total, "minutes has passed starting from 00:00.")
timer = [0, 0, 0, 0]
hours = str(int(minutes_total/60))
minutes = str(minutes_total - int(minutes_total/60)*60)

if len(hours) == 1:
    timer[1] = int(hours)
elif len(hours) == 2:
    timer[0] = int(hours[0])
    timer[1] = int(hours[1])

if len(minutes) == 1:
    timer[3] = int(minutes[0])
elif len(minutes) == 2:
    timer[2] = int(minutes[0])
    timer[3] = int(minutes[1])

current_time = [str(x) for x in timer]
current_time.insert(2, ":")
display_time = ''.join(map(str, current_time))
print("Current time: ", display_time)
print("Sum of time numbers: ", timer[0] + timer[1] + timer[2] + timer[3])

print()

# Level Up (1)
print("--------Task #2 (1): 'Level Up'--------")
XP = 10
threshold = 15
reward = 3
print(XP + reward >= threshold)
print()

# Level Up (2)
print("--------Task #2 (2): 'Level Up'--------")
if XP+reward >= threshold:
    print("You have reached the next level!")
else:
    print("You need", threshold - (XP+reward), "goal(s) to reach the next level.")

print()

# Time converter
print("--------Task #3: 'Time converter'--------")

time24 = "20:01"
time12 = ""
hours = time24[:2]
if int(hours) == 00:
    hours = "12"
    time12 = hours + time24[2:] + " a.m."
elif int(hours) < 12:
    if time24[0] == 0:
        time12 = time24[1:] + " a.m."
    else:
        time12 = time24[:] + " a.m."
elif int(hours) == 12:
    time12 = time24 + " p.m."
elif int(hours) > 12:
    hours = str(int(hours) - 12)
    time12 = hours + time24[2:] + " p.m."

print("Time in 24-hour format:", time24)
print("Time in 12-hour format:", time12)
