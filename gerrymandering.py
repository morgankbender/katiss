# Problem: https://open.kattis.com/problems/gerrymandering

# External imports
import math

# Get first line of input
params = input("").split(" ")

# Init var
n_precinct = int(params[0])
n_district = int(params[1])
votes_a = [0] * n_district
votes_b = [0] * n_district
wasted_a = 0
wasted_b = 0
total_votes = 0

# Get additional lines of input and sort incoming information by
# candidate vote (list) and district (index)
for i in range(n_precinct):
    res = input("").split(" ")
    votes_a[int(res[0]) - 1] += int(res[1])
    votes_b[int(res[0]) - 1] += int(res[2])

# Calculate results for each district
for i in range(n_district):
    # Init district vars
    dist_votes_a = votes_a[i]
    dist_votes_b = votes_b[i]
    dist_total = dist_votes_a + dist_votes_b
    dist_req = math.floor(dist_total / 2) + 1

    # Determine district winner and use that to calculate wasted votes.
    # Print collected information on one line, space separated
    if dist_votes_a > dist_votes_b:
        dist_wasted_a = dist_votes_a - dist_req
        dist_wasted_b = dist_votes_b
        print("A", dist_wasted_a, dist_wasted_b)
    else:
        dist_wasted_a = dist_votes_a
        dist_wasted_b = dist_votes_b - dist_req
        print("B", dist_wasted_a, dist_wasted_b)

    # Add district information to election totals
    wasted_a += dist_wasted_a
    wasted_b += dist_wasted_b
    total_votes += dist_total

# Calculate and print efficiency gap, using election totals
print(abs(wasted_a - wasted_b) / total_votes)
