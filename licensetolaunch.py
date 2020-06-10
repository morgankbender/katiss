# Problem: https://open.kattis.com/problems/licensetolaunch

# Get input
n = int(input(""))
space_junk = input("").split(" ")

# Init var
min_junk = 10**9
launch_day = 0

# Compare each day's amount of space junk to previous lowest.
# Save new date and value if new lowest
for i in range(n):
    if int(space_junk[i]) < min_junk:
        min_junk = int(space_junk[i])
        launch_day = i

# Print launch day
print(launch_day)
