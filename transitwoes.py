# Store all info from lines of input
param = input("").split(" ")
walkTimes = input("").split(" ")
rideTimes = input("").split(" ")
intervals = input("").split(" ")

# Init var
currTime = int(param[0])
n = int(param[2])

# Calculate passing time for each section of the trip
for i in range(n):
    currTime += int(walkTimes[i])
    while currTime % int(intervals[i]) != 0:
        currTime += 1
    currTime += int(rideTimes[i])

# Add time for walk to class after final bus
currTime += int(walkTimes[n])

# Compare time of arrival to time class started
if currTime <= int(param[1]):
    print("yes")
else:
    print("no")
