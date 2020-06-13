# Problem: https://open.kattis.com/problems/fiftyshades

# External imports
import sys

# Throw away first line of input
input("")

# Init var
counter = 0

# Check if each line contains either rose or pink when set to lowercase
for line in sys.stdin:
    if "rose" in line.lower() or "pink" in line.lower():
        counter += 1

# Output final count of boxes with rose or pink (unless the counter
# is at zero, in which case print the excuse)
if counter > 0:
    print(counter)
else:
    print("I must watch Star Wars with my daughter")
