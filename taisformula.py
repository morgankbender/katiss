# Problem: https://open.kattis.com/problems/taisformula

# Get number of data points
n = int(input(""))

# Each calculation requires a point and the point before it. We must
# init first point which is not part of its own calculation (since
# there is nothing before it)
prev_pt = input("").split(" ")
prev_t = float(prev_pt[0])
prev_v = float(prev_pt[1])

# Init the total area var
total_area = 0

# Traverse each point
for i in range(n - 1):
    # Store point
    next_pt = input("").split(" ")
    next_t = float(next_pt[0])
    next_v = float(next_pt[1])

    # Area between two points is a trapezoid. Add to total are
    total_area += ((prev_v + next_v) / 2) * (next_t - prev_t)

    # Point we found in this iteration now becomes "previous point"
    # as we prepare to move to the next point / iteration
    prev_t = next_t
    prev_v = next_v

# Print result
print(total_area / 1000)
