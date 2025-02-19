statues = [6, 2, 3, 8]
statues.sort()
statues_missing = []
count = 0
for x in range(statues[0], statues[-1]):
    if x not in statues:
        statues_missing.append(x)
        count += 1
print("Missing statues:", statues_missing)
print("Number of missing statues:", count)
