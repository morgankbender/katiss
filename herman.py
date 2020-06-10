# Problem: https://open.kattis.com/problems/herman

# External imports
import math

# Get input
r = float(input(""))

# Print output of formula using euclidean algebra, followed by
# taxicab algebra on a new line
print(math.pi * (r ** 2))
print(2 * (r ** 2))
