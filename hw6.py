# Time
print("--------Task #1: 'Time'--------")
minutes_total = 808
print(minutes_total, "minutes have passed since 00:00.")
hours = minutes_total // 60
minutes = minutes_total - (hours * 60)
print("Current time:", f"{hours}:{minutes}")

result = 0
result += sum(int(x) for x in str(hours))
result += sum(int(x) for x in str(minutes))
print("Sum of time numbers:", result)

print()

# Level Up
print("--------Task #2: 'Level Up'--------")
XP = 10
threshold = 15
reward = 3
if XP+reward >= threshold:
    print("You have reached the next level!")
else:
    print("You need", threshold - (XP+reward), "goal(s) to reach the next level.")

print()

# Time converter
print("--------Task #3: 'Time converter'--------")

time24 = input("Please, enter time in HH:MM format: ")
time24_split = time24.split(":")
hh = int(time24_split[0])
mm = time24_split[1]

if hh >= 12:
    if hh > 12:
        hh -= 12
    daytime = "p.m."
else:
    if hh == 0:
        hh = 12
    daytime = "a.m."

print("Time in 24-hour format:", time24)
print("Time in 12-hour format:", f"{hh}:{mm} {daytime}")
